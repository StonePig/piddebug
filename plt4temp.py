# -*- coding: utf-8 -*-
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from pylab import *
from matplotlib.widgets import Button
from kneed import KneeLocator

running_dict = {
    '0':'init',
    '1':'首出水',
    '2':'常温',
    '3':'强抽',
    '4':'预热',
    '5':'加热',
    '6':'反向',
    '7':'保护',
}



b_flow = [0] * 500
b_temp_in = [0] * 500
b_temp_out = [0] * 500
b_sum_error = [0] * 500
b_other = [0] * 500
b_kp = [0] * 500
b_ki = [0] * 500
PID_Out = [0] * 500
sample_time = np.arange(500)
is_play = True
update_data_flag = True
counter = 0
SumError = 0
pid_out = 0
lastError = 0

def update_data(temp_in, temp_out, flow, sum_error, other):
    global update_data_flag
    global counter
    global SumError
    global pid_out
    global lastError

    # if(flow < 300 and temp < 10000):
    if(temp_out < 11000):
        b_flow.pop(0)
        b_flow.append(flow)
        b_temp_in.pop(0)
        b_temp_in.append(round(temp_in/100, 1))
        b_temp_out.pop(0)
        b_temp_out.append(round(temp_out/100, 1))        
        b_sum_error.pop(0)
        b_sum_error.append((sum_error + 30000) / 205 )
        b_other.pop(0)
        b_other.append(other)
        # b_kp.pop(0)
        # b_kp.append(kp)
        # b_ki.pop(0)
        # b_ki.append(ki)
        update_data_flag = True
        counter += 1

        # if(flow == 0):
        #     SumError = 0
        #     pid_out = 0
        #     lastError = 0
        #     sum = 0
        # else:
        #     thisError = 8000 - temp
        #     D_Error = thisError - lastError
        #     lastError = thisError; 

        #     if(thisError < 200):
        #         SumError += (thisError >> 7)
        #     elif(thisError < 2000):
        #         SumError += (thisError >> 7)      
        #     else:
        #         SumError += (thisError >> 8)

        #     if(SumError > 2000):
        #         SumError = 2000
        #     if(SumError < -2000): 
        #         SumError = -2000
        #     sum = 8 * thisError + 3 * SumError + 50 * D_Error

        #     if(sum > 15000):
        #         sum = 15000

        #     if(sum < -3000):
        #         sum = -3000

        # PID_Out.pop(0)
        # PID_Out.append(SumError)



def func(event):
    print("button clicked!")

def onpress(event):
    global is_play
    if(is_play is True):
        is_play = False
    else:
        is_play = True

def update_picture():
    global is_play
    global update_data_flag
    global counter

    rc('mathtext', default='regular')
    mpl.rcParams['font.sans-serif'] = ['SimHei']  # 添加这条可以让图形显示中文
    plt.ion() #开启interactive mode 成功的关键函数
    figID="温度走势"
    fig=plt.figure(figID)  
    cid_press   = fig.canvas.mpl_connect('button_press_event'  , onpress  )

    # mng = plt.get_current_fig_manager()
    # mng.window.state("zoomed")

    counter = 0
    heat_num = 0

    while(True):
        if not plt.fignum_exists(figID):
            break        
        plt.clf()  #清除上一幅图像

        # ax2 = fig.add_subplot(211)
        # ax = fig.add_subplot(212)
        ax2 = fig.add_subplot(111)
        ax = ax2.twinx()
        # ax_temp_in = ax2.twinx()
        # ax_sum_error = ax2.twinx()

        # ax_ki = ax2.twinx()

        lns1 = ax2.plot(sample_time, b_flow, '-', label = '流速')
        lns2 = ax.plot(sample_time, b_temp_out, '-r', label = '出水温度')
        lns3 = ax.plot(sample_time, b_temp_in, '-b', label = '进水温度')
        lns4 = ax2.plot(sample_time, b_sum_error, '-y', label = 'PID_OUT')


        # ax.yaxis.set_ticks([25,45,55,80,90,95,100])
        ax.yaxis.set_ticks([0,25,45,55,65,75,85,95,100])
        ax.grid(linestyle=":", axis="both")
        ax.set_ylabel(r"温度 ($^\circ$C)")
        ax.set_ylim(0, 110)


        ax2.set_xlabel("Time (ms), heat num:" + '{:d}'.format(heat_num) + ' time:' + '{:d}'.format(counter))
        ax2.set_ylabel(r"流速")
        ax2.set_ylim(0,300)
        # ax2.set_ylim(-3100,3100)
        ax2.grid(linestyle=":", axis="x")


        # added these lines
        lns = lns1+lns2+lns3+lns4
        labs = [l.get_label() for l in lns]
        ax.legend(lns, labs, loc=2)

        y1_min=np.argmin(b_temp_out)
        y1_max=np.argmax(b_temp_out)

        show_min='['+str(y1_min)+' '+str(b_temp_out[y1_min])+']'
        
        # 以●绘制最大值点和最小值点的位置
        # plt.plot(y1_min,b_temp[y1_min],'ko') 
        plt.plot(y1_max,b_temp_out[y1_max],'ko')

        running_state_prev = 0
        debug_msg_prev = 0
        for i in range(len(b_other) - 1):
            debug_msg = int(b_other[i] / 256)
            running_state = int((b_other[i] & 0xFF) / 16)
            heat_num = b_other[i] & 0x0F

            # 温度稳定条件
            if(debug_msg == 3):
                plt.plot(i,b_temp_out[i],'k^')

            # 固定pwm输出
            # if(debug_msg == 1 and debug_msg_prev == 0):
            #     plt.plot(i,b_temp_out[i],'r^')

            # pid 启动
            if(debug_msg == 2 and debug_msg_prev == 1):
                plt.plot(i,b_temp_out[i],'r^')

            # 状态发生变化
            if(running_state != running_state_prev):
                plt.plot(i,b_temp_out[i],'k^')
                show_text = '[' + running_dict[str(running_state)] + ']'
                plt.annotate(show_text,xy=(i,b_temp_out[i]),xytext=(i,b_temp_out[i]))

            running_state_prev = running_state
            debug_msg_prev = debug_msg
            
                # show_max='['+str(b_ki[i + 1])+']'

        show_max='['+str(b_temp_out[y1_max])+']'
        plt.annotate(show_max,xy=(y1_max,b_temp_out[y1_max]),xytext=(y1_max,b_temp_out[y1_max]))

        # x, y = sample_time, b_temp
        # output_knees = []
        # for curve in ['convex', 'concave']:
        #     for direction in ['increasing', 'decreasing']:
        #         model = KneeLocator(x=x, y=y, curve=curve, direction=direction, online=True)
        #         if len(model.all_knees):
        #             # print((model.knee, model.knee_y, curve, direction))  
        #             # show_max = '['+str(model.knee_y)+']'
        #             plt.plot(list(model.all_knees),model.all_knees_y,'ko')    
                    # plt.annotate(show_max,xy=(model.knee,model.knee_y),xytext=(model.knee,model.knee_y))

        if(update_data_flag):
            plt.savefig('E:/git/ecu_simu/python/static/0.png')
        
        update_data_flag = False

        # buttonaxe = plt.axes([0.89, 0.01, 0.1, 0.075])
        # button1 = Button(buttonaxe, 'pause')
        # button1.on_clicked(func) 

        
        
        # plt.ion()
        while(is_play is False):
            plt.pause(0.01)  
            if not plt.fignum_exists(figID):
                break    
        plt.pause(0.01)  # 暂停0.01秒
        plt.ioff()  # 关闭画图的窗口

        # plt.show()
        # plt.draw()#注意此函数需要调用
        # time.sleep(1)

if __name__ == '__main__':

    i=0

    while i<500:
        b_flow.pop(0)
        b_flow.append(i)
        b_temp_in.pop(0)
        b_temp_in.append(i*2)
        b_temp_out.pop(0)
        b_temp_out.append(i*3)    
        b_sum_error.pop(0)
        b_sum_error.append(i*4)  
        b_other.pop(0)
        b_other.append(i*5)                             
        i = i + 1


    update_picture()