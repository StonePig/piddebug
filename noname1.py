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
		self.m_comboBox_Port = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox_PortChoices, 0 )
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
		
		
		gSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer5.SetMinSize( wx.Size( -1,50 ) ) 
		self.m_staticText_powe1 = wx.StaticText( self, wx.ID_ANY, u"有功功率", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_powe1.Wrap( -1 )
		bSizer5.Add( self.m_staticText_powe1, 0, wx.ALL, 5 )
		
		self.m_textCtrl_power1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_textCtrl_power1, 0, wx.ALL, 5 )
		
		self.m_staticText_power2 = wx.StaticText( self, wx.ID_ANY, u"无功功率", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_power2.Wrap( -1 )
		bSizer5.Add( self.m_staticText_power2, 0, wx.ALL, 5 )
		
		self.m_textCtrl_power2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_textCtrl_power2, 0, wx.ALL, 5 )
		
		self.m_staticText_power = wx.StaticText( self, wx.ID_ANY, u"视在功率", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_power.Wrap( -1 )
		bSizer5.Add( self.m_staticText_power, 0, wx.ALL, 5 )
		
		self.m_textCtrl_power = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_textCtrl_power, 0, wx.ALL, 5 )
		
		
		gSizer1.Add( bSizer5, 1, wx.ALL, 5 )
		
		self.m_textCtrl_PRM = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_textCtrl_PRM, 0, wx.ALL, 5 )
		
		self.m_staticText_PRM = wx.StaticText( self, wx.ID_ANY, u"Engineer Speed", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_PRM.Wrap( -1 )
		self.m_staticText_PRM.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText_PRM.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		gSizer1.Add( self.m_staticText_PRM, 0, wx.ALL, 5 )
		
		
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
	
	def send_to_slave_timer( self, event ):
		event.Skip()
	

