# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class modbusApp
###########################################################################

class modbusApp ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"modbus app", pos = wx.DefaultPosition, size = wx.Size( 901,515 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		gSizer1 = wx.GridSizer( 10, 1, 0, 0 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"串口", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer3.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		m_comboBox_PortChoices = []
		self.m_comboBox_Port = wx.ComboBox( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, m_comboBox_PortChoices, 0 )
		bSizer3.Add( self.m_comboBox_Port, 0, wx.ALL, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"波特率", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer3.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		m_comboBox_BaudChoices = [ u"9600", u"19200", u"38400", u"115200" ]
		self.m_comboBox_Baud = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox_BaudChoices, 0 )
		self.m_comboBox_Baud.SetSelection( 0 )
		bSizer3.Add( self.m_comboBox_Baud, 0, wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"设备地址", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer3.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.m_textCtrl_SlaveAddr = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer3.Add( self.m_textCtrl_SlaveAddr, 0, wx.ALL, 5 )
		
		self.m_button_port_open = wx.Button( self, wx.ID_ANY, u"打开", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button_port_open, 0, wx.ALL, 5 )
		
		
		gSizer1.Add( bSizer3, 1, wx.EXPAND, 9 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer5.SetMinSize( wx.Size( -1,50 ) ) 
		m_comboBox_tempChoices = [ u"45", u"55", u"80", u"90", u"95" ]
		self.m_comboBox_temp = wx.ComboBox( self, wx.ID_ANY, u"45", wx.DefaultPosition, wx.DefaultSize, m_comboBox_tempChoices, 0 )
		bSizer5.Add( self.m_comboBox_temp, 0, wx.ALL, 5 )
		
		self.m_staticText_kp = wx.StaticText( self, wx.ID_ANY, u"kp", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_kp.Wrap( -1 )
		bSizer5.Add( self.m_staticText_kp, 0, wx.ALL, 5 )
		
		self.m_textCtrl_kp = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_textCtrl_kp, 0, wx.ALL, 5 )
		
		self.m_staticText_ki = wx.StaticText( self, wx.ID_ANY, u"ki", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_ki.Wrap( -1 )
		bSizer5.Add( self.m_staticText_ki, 0, wx.ALL, 5 )
		
		self.m_textCtrl_ki = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_textCtrl_ki, 0, wx.ALL, 5 )
		
		self.m_staticText_kd = wx.StaticText( self, wx.ID_ANY, u"kd", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_kd.Wrap( -1 )
		bSizer5.Add( self.m_staticText_kd, 0, wx.ALL, 5 )
		
		self.m_textCtrl_kd = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_textCtrl_kd, 0, wx.ALL, 5 )
		
		self.m_staticText_pwm = wx.StaticText( self, wx.ID_ANY, u"max", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_pwm.Wrap( -1 )
		bSizer5.Add( self.m_staticText_pwm, 0, wx.ALL, 5 )
		
		self.m_textCtrl_pwm = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_textCtrl_pwm, 0, wx.ALL, 5 )
		
		self.m_button_setting = wx.Button( self, wx.ID_ANY, u"设置", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button_setting, 0, wx.ALL, 5 )
		
		self.m_button_open = wx.Button( self, wx.ID_ANY, u"open", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button_open, 0, wx.ALL, 5 )
		
		
		gSizer1.Add( bSizer5, 1, wx.ALL, 5 )
		
		bSizer31 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"电压：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		bSizer31.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		m_comboBox_voutChoices = [ u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7" ]
		self.m_comboBox_vout = wx.ComboBox( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, m_comboBox_voutChoices, 0 )
		bSizer31.Add( self.m_comboBox_vout, 0, wx.ALL, 5 )
		
		self.m_vout = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer31.Add( self.m_vout, 0, wx.ALL, 5 )
		
		self.m_set_vout = wx.Button( self, wx.ID_ANY, u"设置", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer31.Add( self.m_set_vout, 0, wx.ALL, 5 )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"DO：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		bSizer31.Add( self.m_staticText9, 0, wx.ALL, 5 )
		
		m_comboBox_doChoices = [ u"0", u"1", u"2", u"3", u"4", u"5" ]
		self.m_comboBox_do = wx.ComboBox( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, m_comboBox_doChoices, 0 )
		bSizer31.Add( self.m_comboBox_do, 0, wx.ALL, 5 )
		
		self.m_do = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer31.Add( self.m_do, 0, wx.ALL, 5 )
		
		self.m_set_do = wx.Button( self, wx.ID_ANY, u"设置", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer31.Add( self.m_set_do, 0, wx.ALL, 5 )
		
		self.m_staticText91 = wx.StaticText( self, wx.ID_ANY, u"SW：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText91.Wrap( -1 )
		bSizer31.Add( self.m_staticText91, 0, wx.ALL, 5 )
		
		m_comboBox_swChoices = [ u"0", u"1", u"2", u"3", u"4", u"5", u"6" ]
		self.m_comboBox_sw = wx.ComboBox( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, m_comboBox_swChoices, 0 )
		bSizer31.Add( self.m_comboBox_sw, 0, wx.ALL, 5 )
		
		self.m_sw = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer31.Add( self.m_sw, 0, wx.ALL, 5 )
		
		self.m_set_sw = wx.Button( self, wx.ID_ANY, u"设置", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer31.Add( self.m_set_sw, 0, wx.ALL, 5 )
		
		
		gSizer1.Add( bSizer31, 1, wx.EXPAND, 5 )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer6.SetMinSize( wx.Size( 300,200 ) ) 
		self.m_button_get_adc = wx.Button( self, wx.ID_ANY, u"get adc", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button_get_adc, 0, wx.ALL, 5 )
		
		self.m_textCtrl_getadc = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 270,200 ), wx.TE_MULTILINE|wx.VSCROLL )
		bSizer6.Add( self.m_textCtrl_getadc, 0, wx.ALL, 5 )
		
		
		gSizer1.Add( bSizer6, 1, wx.ALIGN_TOP|wx.BOTTOM, 5 )
		
		
		self.SetSizer( gSizer1 )
		self.Layout()
		self.m_timer_query_slave = wx.Timer()
		self.m_timer_query_slave.SetOwner( self, wx.ID_ANY )
		self.m_timer_query_slave.Start( 200 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_comboBox_Port.Bind( wx.EVT_COMBOBOX, self.PortSelectNewVaule )
		self.m_comboBox_Baud.Bind( wx.EVT_COMBOBOX, self.BaudSelectNewVaule )
		self.m_textCtrl_SlaveAddr.Bind( wx.EVT_TEXT_ENTER, self.SlaveAddrEnter )
		self.m_button_port_open.Bind( wx.EVT_BUTTON, self.PortOpen )
		self.m_comboBox_temp.Bind( wx.EVT_COMBOBOX, self.m_comboBox_tempOnCombobox )
		self.m_button_setting.Bind( wx.EVT_BUTTON, self.OnsettingButtonClick )
		self.m_button_open.Bind( wx.EVT_BUTTON, self.m_button_openOnButtonClick )
		self.m_comboBox_vout.Bind( wx.EVT_COMBOBOX, self.m_comboBox_voutOnCombobox )
		self.m_set_vout.Bind( wx.EVT_BUTTON, self.m_button_setting_vout )
		self.m_comboBox_do.Bind( wx.EVT_COMBOBOX, self.m_comboBox_doOnCombobox )
		self.m_set_do.Bind( wx.EVT_BUTTON, self.m_button_do )
		self.m_comboBox_sw.Bind( wx.EVT_COMBOBOX, self.m_comboBox_doOnCombobox )
		self.m_set_sw.Bind( wx.EVT_BUTTON, self.m_button_sw )
		self.m_button_get_adc.Bind( wx.EVT_BUTTON, self.m_button_getadc )
		self.Bind( wx.EVT_TIMER, self.send_to_slave_timer, id=wx.ID_ANY )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def PortSelectNewVaule( self, event ):
		event.Skip()
	
	def BaudSelectNewVaule( self, event ):
		event.Skip()
	
	def SlaveAddrEnter( self, event ):
		event.Skip()
	
	def PortOpen( self, event ):
		event.Skip()
	
	def m_comboBox_tempOnCombobox( self, event ):
		event.Skip()
	
	def OnsettingButtonClick( self, event ):
		event.Skip()
	
	def m_button_openOnButtonClick( self, event ):
		event.Skip()
	
	def m_comboBox_voutOnCombobox( self, event ):
		event.Skip()
	
	def m_button_setting_vout( self, event ):
		event.Skip()
	
	def m_comboBox_doOnCombobox( self, event ):
		event.Skip()
	
	def m_button_do( self, event ):
		event.Skip()
	
	
	def m_button_sw( self, event ):
		event.Skip()
	
	def m_button_getadc( self, event ):
		event.Skip()
	
	def send_to_slave_timer( self, event ):
		event.Skip()
	

