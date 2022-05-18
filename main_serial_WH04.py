# -*- coding: utf-8 -*- 

import wx
# 导入modbus_win.py中内容
import serial_app_win
import win32api,win32con
from tkinter.filedialog import askdirectory
import time
from serial.tools import list_ports
import serial

import _thread
import threading

import configparser

import re

from plt4temp import *

from multiprocessing import Process
import tkinter as tk
from tkinter import filedialog

# 创建mainWin类并传入modbus_win.MyFrame1
class mainWin(serial_app_win.serialApp):
	port_opened = False

	def init(self):

		ret1 = re.findall('\d+', "Content length:1000;Package Length:1234;")

		str_ = "Content length:1000;Package Length:1234;"
		number = re.findall("\d+",str_)    # 输出结果为列表
		print(number)


		self.init_done = True

		self.config = configparser.ConfigParser()
		self.cfg_file = "./config.ini"
		self.config.read(self.cfg_file)
		
		self.baudrate = self.config.get('DEFAULT', 'baud')
		if self.baudrate in self.m_comboBox_Baud.GetItems():
			self.m_comboBox_Baud.SetSelection(self.m_comboBox_Baud.FindString(self.baudrate, False))
		else:
			self.baudrate = "9600"
			print("配置文件错误：不支持的波特率")
			win32api.MessageBox(0, "配置文件错误：不支持的波特率", "提醒",win32con.MB_ICONWARNING)
			self.init_done = False

		self.kp = self.config.get('DEFAULT', 'kp_45')
		self.ki = self.config.get('DEFAULT', 'ki_45')
		self.kd = self.config.get('DEFAULT', 'kd_45')
		self.pwm = self.config.get('DEFAULT', 'pwm_45')

		self.m_textCtrl_kp.SetValue(self.kp)
		self.m_textCtrl_ki.SetValue(self.ki)
		self.m_textCtrl_kd.SetValue(self.kd)
		self.m_textCtrl_pwm.SetValue(self.pwm)

		self.m_comboBox_temp.SetSelection(0)


		port_list = list(list_ports.comports())
		num = len(port_list)
		if num <= 0:
			print("找不到任何串口设备")
			# win32api.MessageBox(0, "找不到任何串口设备", "提醒",win32con.MB_ICONWARNING)
			self.init_done = False
		else:
			port_items = []
			for i in range(num):
				# 将 ListPortInfo 对象转化为 list
				port = list(port_list[i])
				port_items.append(port[0]) 
				print(port_list)
				print(port_list[i])
				print(port)
				print(port_items)

			self.m_comboBox_Port.Set(port_items)
			self.port = self.config.get('DEFAULT', 'port')
			if self.port in self.m_comboBox_Port.GetItems():
				self.m_comboBox_Port.SetSelection(self.m_comboBox_Port.FindString(self.port, False))
			else:
				self.m_comboBox_Port.SetSelection(0)

			self.port = self.m_comboBox_Port.GetValue()


	def send_to_slave_timer(self, event ):
		pass
			
	def PortSelectNewVaule( self, event ):
		print(self.m_comboBox_Port.GetValue())
		self.port = self.m_comboBox_Port.GetValue()
		self.config.set('DEFAULT', 'port', self.port)
	
	def BaudSelectNewVaule( self, event ):
		print(self.m_comboBox_Baud.GetValue())
		self.baudrate = self.m_comboBox_Baud.GetValue()
		self.config.set('DEFAULT', 'baud', self.baudrate)

	def recv(self, com):
		data = b''
		print("recv thread start")
		file_name = "log/record_" + time.strftime("%Y%m%d%H%M%S", time.localtime()) + ".csv"
		with open(file_name, 'w', encoding='utf-8') as fo:
			fo.write('time,temp in,temp out,flow,sum,heat_num,state' + '\n')
			while (self.port_opened):
				time.sleep(0.01)
				try:
					n = com.inWaiting()
					if n:
						data = data + com.read(n)
					else:
						data_len = len(data)
						if(data_len != 0):
							print(len(data),data)
							data_len = len(data)
							rec_len = 10
							if(data_len % rec_len ==0):
								for i in range(0, data_len // rec_len):
									temp_in = data[i * rec_len + 1] + data[i * rec_len + 0] * 256
									temp_out = data[i * rec_len + 3] + data[i * rec_len + 2] * 256
									flow = data[i * rec_len + 5] + data[i * rec_len + 4] * 256
									sum_error = data[i * rec_len + 7] + data[i * rec_len + 6] * 256
									other = data[i * rec_len + 9] + data[i * rec_len + 8] * 256

									if(temp_in > 40000):
										temp_in = temp_in - 0x10000
									if(temp_out > 40000):
										temp_out = temp_out - 0x10000
									if(sum_error > 40000):
										sum_error = sum_error - 0x10000																				
									# if(other > 40000):
									# 	other = other - 0x10000

									debug_msg = int(other / 256)
									running_state = int((other & 0xFF) / 16)
									heat_num = other & 0x0F

									
									update_data(temp_in, temp_out, flow, sum_error, other)
									record_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ":" + str(int(round(time.time() * 10)) % 10)
									fo.write(record_time + ',' + str(temp_in) + ',' + str(temp_out) +  ',' + str(flow)  + ',' + str(sum_error)  + ',' + str(heat_num) + ',' + str(running_state) + "\n")

							data = b''

				except Exception as exc:
					return

		return

	
	def PortOpen( self, event ):
		if(self.init_done == False):
			return

		if(self.port_opened == False):	
			self.m_button_port_open.SetLabel("关闭")
			try:
				self.com = serial.Serial(port=self.port,baudrate=self.baudrate, bytesize=8, parity='N', stopbits=1)
			except Exception as exc:
				win32api.MessageBox(0, "串口打开失败", "提醒",win32con.MB_ICONWARNING)
				return
			if self.com.isOpen() :
				self.port_opened = True
				print("open success")
				# _thread.start_new_thread(update_picture, ())
				_thread.start_new_thread(self.recv, (self.com,))
				update_picture()
			else :
				print("open failed")
				win32api.MessageBox(0, "串口打开失败", "提醒",win32con.MB_ICONWARNING)
				return
		
			self.m_comboBox_Port.Disable()
			self.m_comboBox_Baud.Disable()
			
			with open(self.cfg_file, 'w', encoding='utf-8') as configfile:
				self.config.write(configfile)
	
			# p_one = Process(target=self.recv)
			# p_one.start()

		else:
			self.port_opened = False
			self.m_button_port_open.SetLabel("打开")
			# serial.Serial.close(self)
			self.com.close()
			self.m_comboBox_Port.Enable()
			self.m_comboBox_Baud.Enable()

	def readfile(self):
		'''打开选择文件夹对话框'''
		root = tk.Tk()
		root.withdraw()
		Filepath = filedialog.askopenfilename() #获得选择好的文件
		print('Filepath:',Filepath)

		# update_picture()
		counter = 0
		delta_ki = 0
		tempList = [0] * 100
		pre = 0
		counter1 = 0

		num = 10

		with open(Filepath, 'r', encoding='utf-8') as f:
			line = f.readline()
			while self.openfile:
				line = f.readline()
				if(line):
					try:
						temp_in = int(line.split(",")[1])
						temp_out = int(line.split(",")[2])		
						flow = int(line.split(",")[3])
						sum_error = int(line.split(",")[4])
						other = int(line.split(",")[5])
					except Exception as exc:
						temp_in = 0
						temp_out = 0
						flow = 0
						sum_error = 0
						other = 0
					
					# t = int(temp_out)
					# tempList[counter % num] = t

					# tempMin = 10000
					# tempMax = 0
					# for i in range(num):
					# 	if(tempList[i] > tempMax):
					# 		tempMax = tempList[i]
					# 	if(tempList[i] < tempMin):
					# 		tempMin = tempList[i]

					# thisError = 8000 - t

					# counter = counter + 1
					# counter1 = counter1 + 1

					# if(counter > num):
					# 	if(thisError > 3000):
					# 		diffTemp = 40
					# 	elif(thisError > 2000):
					# 		diffTemp = 50
					# 	elif(thisError > 1000):
					# 		diffTemp = 40
					# 	elif(thisError > 200):
					# 		diffTemp = 30
					# 	else:
					# 		diffTemp = 0
					# 	if(tempMax - tempMin < diffTemp):
					# 		counter = 0
					# 		if(flow != 0):
					# 			if(counter1 < pre + 50):
					# 				delta_ki += 2
					# 				kp = 0
					# 			else:
					# 				kp = 1

					# 		pre = counter1

					# if(flow == 0):
					# 	delta_ki = 0
					# ki += delta_ki


					update_data(temp_in, temp_out, flow, sum_error, other)
					
					# print(flow, temp)
				else:
					break
				time.sleep(0.01)
		root.mainloop()

	def m_button_openOnButtonClick( self, event ):
		self.openfile = False
		time.sleep(0.5)
		self.openfile = True
		_thread.start_new_thread(self.readfile, ())
		update_picture()

	def m_comboBox_tempOnCombobox( self, event ):	
		self.temp = self.m_comboBox_temp.GetValue()
		kp_temp = "kp_" + self.temp
		ki_temp = "ki_" + self.temp
		kd_temp = "kd_" + self.temp
		pwm_temp = "pwm_" + self.temp

		self.kp = self.config.get('DEFAULT', kp_temp)
		self.ki = self.config.get('DEFAULT', ki_temp)
		self.kd = self.config.get('DEFAULT', kd_temp)
		self.pwm = self.config.get('DEFAULT', pwm_temp)		

		self.m_textCtrl_kp.SetValue(self.kp)
		self.m_textCtrl_ki.SetValue(self.ki)
		self.m_textCtrl_kd.SetValue(self.kd)
		self.m_textCtrl_pwm.SetValue(self.pwm)



	def OnsettingButtonClick( self, event ):
		if (self.port_opened):
			self.temp = self.m_comboBox_temp.GetValue()
			kp_temp = "kp_" + self.temp
			ki_temp = "ki_" + self.temp
			kd_temp = "kd_" + self.temp
			pwm_temp = "pwm_" + self.temp

			self.kp = self.m_textCtrl_kp.GetValue()
			self.ki = self.m_textCtrl_ki.GetValue()
			self.kd = self.m_textCtrl_kd.GetValue()
			self.pwm = self.m_textCtrl_pwm.GetValue()

			self.config.set('DEFAULT', kp_temp, self.kp)
			self.config.set('DEFAULT', ki_temp, self.ki)
			self.config.set('DEFAULT', kd_temp, self.kd)
			self.config.set('DEFAULT', pwm_temp, self.pwm)
			with open(self.cfg_file, 'w', encoding='utf-8') as configfile:
				self.config.write(configfile)

			sendbuf = b''
			sel = self.m_comboBox_temp.GetSelection()
			print(sel)
			sendbuf += int(sel).to_bytes(1,'little')
			sendbuf += int(self.kp).to_bytes(1,'little')
			sendbuf += int(self.ki).to_bytes(1,'little')
			sendbuf += int(self.kd).to_bytes(1,'little')
			sendbuf += int(self.pwm).to_bytes(1,'little')
			# sendbuf += int(self.pwm).to_bytes(1,'little')

			self.com.write(sendbuf)

		else:
			win32api.MessageBox(0, "串口未打开", "提醒",win32con.MB_ICONWARNING)
			import numpy as np
			# 读取文件，文件绝对地址"D:\Project\arpatest01\foo.arpa"
			dat = np.fromfile("C:\\Users\\yaozhong\\Desktop\\ee2.bin", dtype=np.uint8)
			print(dat.shape)# 打印二进制文件形状
			# 打印前一百个字符
			num = dat[0]
			step = num / 10
			for i in range(1, 10):
				# print(dat[i]*256+dat[i+1])
				start = int(step * i)
				diff = int((step * i - start) * 10)
				value_start = dat[start*2] * 256 + dat[start*2+1]
				value_end = dat[start*2 + 2] * 256 + dat[start*2+3]
				mod1 =  round(diff * (value_start - value_end) / 10)
				value = value_start - mod1
				print(value)



if __name__ == '__main__':
	# 下面是使用wxPython的固定用法
	app = wx.App()
	main_win = mainWin(None)
	main_win.Show()
	main_win.init()
	app.MainLoop()