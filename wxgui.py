# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jan 23 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tunneler", pos = wx.DefaultPosition, size = wx.Size( 220,370 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.panel_main = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer1 = wx.GridSizer( 5, 5, 0, 0 )
		
		self.m_checkBox1 = wx.CheckBox( self.panel_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox1.SetValue(True) 
		gSizer1.Add( self.m_checkBox1, 0, wx.ALL, 5 )
		
		self.m_checkBox2 = wx.CheckBox( self.panel_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox2.SetValue(True) 
		gSizer1.Add( self.m_checkBox2, 0, wx.ALL, 5 )
		
		self.m_checkBox3 = wx.CheckBox( self.panel_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox3.SetValue(True) 
		gSizer1.Add( self.m_checkBox3, 0, wx.ALL, 5 )
		
		self.m_checkBox4 = wx.CheckBox( self.panel_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox4.SetValue(True) 
		gSizer1.Add( self.m_checkBox4, 0, wx.ALL, 5 )
		
		self.check_box_end = wx.CheckBox( self.panel_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.check_box_end.Enable( False )
		
		gSizer1.Add( self.check_box_end, 0, wx.ALL, 5 )
		
		self.m_checkBox6 = wx.CheckBox( self.panel_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox6.SetValue(True) 
		gSizer1.Add( self.m_checkBox6, 0, wx.ALL, 5 )
		
		self.m_checkBox7 = wx.CheckBox( self.panel_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox7.SetValue(True) 
		gSizer1.Add( self.m_checkBox7, 0, wx.ALL, 5 )
		
		self.m_checkBox8 = wx.CheckBox( self.panel_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox8.SetValue(True) 
		gSizer1.Add( self.m_checkBox8, 0, wx.ALL, 5 )
		
		self.m_checkBox9 = wx.CheckBox( self.panel_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox9.SetValue(True) 
		gSizer1.Add( self.m_checkBox9, 0, wx.ALL, 5 )
		
		self.m_checkBox10 = wx.CheckBox( self.panel_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox10.SetValue(True) 
		gSizer1.Add( self.m_checkBox10, 0, wx.ALL, 5 )
		
		self.m_checkBox11 = wx.CheckBox( self.panel_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox11.SetValue(True) 
		gSizer1.Add( self.m_checkBox11, 0, wx.ALL, 5 )
		
		self.m_checkBox12 = wx.CheckBox( self.panel_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox12.SetValue(True) 
		gSizer1.Add( self.m_checkBox12, 0, wx.ALL, 5 )
		
		self.m_checkBox13 = wx.CheckBox( self.panel_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox13.SetValue(True) 
		gSizer1.Add( self.m_checkBox13, 0, wx.ALL, 5 )
		
		self.m_checkBox14 = wx.CheckBox( self.panel_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox14.SetValue(True) 
		gSizer1.Add( self.m_checkBox14, 0, wx.ALL, 5 )
		
		self.m_checkBox15 = wx.CheckBox( self.panel_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox15.SetValue(True) 
		gSizer1.Add( self.m_checkBox15, 0, wx.ALL, 5 )
		
		self.m_checkBox16 = wx.CheckBox( self.panel_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox16.SetValue(True) 
		gSizer1.Add( self.m_checkBox16, 0, wx.ALL, 5 )
		
		self.m_checkBox17 = wx.CheckBox( self.panel_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox17.SetValue(True) 
		gSizer1.Add( self.m_checkBox17, 0, wx.ALL, 5 )
		
		self.m_checkBox18 = wx.CheckBox( self.panel_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox18.SetValue(True) 
		gSizer1.Add( self.m_checkBox18, 0, wx.ALL, 5 )
		
		self.m_checkBox19 = wx.CheckBox( self.panel_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox19.SetValue(True) 
		gSizer1.Add( self.m_checkBox19, 0, wx.ALL, 5 )
		
		self.m_checkBox20 = wx.CheckBox( self.panel_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox20.SetValue(True) 
		gSizer1.Add( self.m_checkBox20, 0, wx.ALL, 5 )
		
		self.check_box_start = wx.CheckBox( self.panel_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.check_box_start.Enable( False )
		
		gSizer1.Add( self.check_box_start, 0, wx.ALL, 5 )
		
		self.m_checkBox22 = wx.CheckBox( self.panel_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox22.SetValue(True) 
		gSizer1.Add( self.m_checkBox22, 0, wx.ALL, 5 )
		
		self.m_checkBox23 = wx.CheckBox( self.panel_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox23.SetValue(True) 
		gSizer1.Add( self.m_checkBox23, 0, wx.ALL, 5 )
		
		self.m_checkBox24 = wx.CheckBox( self.panel_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox24.SetValue(True) 
		gSizer1.Add( self.m_checkBox24, 0, wx.ALL, 5 )
		
		self.m_checkBox25 = wx.CheckBox( self.panel_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox25.SetValue(True) 
		gSizer1.Add( self.m_checkBox25, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self.panel_main, wx.ID_ANY, u"Solves fastest path from bottom left to top right. No diagonals. Checkmarks are walls which take 7 steps to destroy and 1 step to walk to.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer3.Add( self.m_staticText1, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.button_solve = wx.Button( self.panel_main, wx.ID_ANY, u"Solve", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.button_solve, 0, wx.ALL, 5 )
		
		self.static_text_status = wx.StaticText( self.panel_main, wx.ID_ANY, u"Ready", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.static_text_status.Wrap( -1 )
		bSizer4.Add( self.static_text_status, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer3.Add( bSizer4, 0, wx.EXPAND, 5 )
		
		
		bSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		
		self.panel_main.SetSizer( bSizer2 )
		self.panel_main.Layout()
		bSizer2.Fit( self.panel_main )
		bSizer1.Add( self.panel_main, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.app_close )
		self.button_solve.Bind( wx.EVT_BUTTON, self.solve_click )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def app_close( self, event ):
		event.Skip()
	
	def solve_click( self, event ):
		event.Skip()
	

