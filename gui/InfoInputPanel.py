#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import wx
import wx.xrc

class InfoInputPanel ( wx.Panel ):
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, 
                size = wx.DefaultSize, style = wx.TAB_TRAVERSAL )
        
        m_OutermostGBSizer = wx.GridBagSizer( 0, 0 )
        m_OutermostGBSizer.SetFlexibleDirection( wx.BOTH )
        m_OutermostGBSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        m_OutermostGBSizer.Add( self.get_InputInfoArea( "Input Informations"),
                wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
     
        m_OutermostGBSizer.Add( self.getControlInfoArea("Control Area"),
                wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
        
        m_OutermostGBSizer.AddGrowableCol( 0 )
        m_OutermostGBSizer.AddGrowableCol( 1 )
        m_OutermostGBSizer.AddGrowableRow( 0 )
        
        self.SetSizer( m_OutermostGBSizer )
        self.Layout()
 
    def get_InputInfoArea(self,label):
        InputsSBSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, label ), wx.VERTICAL )
        
        CellsFGSizer = wx.FlexGridSizer( 0, 2, 0, 0 )

        CellsFGSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        input_list = ['First Name','Last Name','Home Address','Email Address']

        for label in input_list:
            self.addStaticText(InputsSBSizer,label,CellsFGSizer)
            self.addTextCtrl(InputsSBSizer,CellsFGSizer)

                
        InputsSBSizer.Add( CellsFGSizer, 1, wx.EXPAND, 5 )
        return InputsSBSizer;

    def addStaticText(self,parent,label,holder):
        staticText = wx.StaticText(parent.GetStaticBox(), wx.ID_ANY,label, wx.DefaultPosition, wx.DefaultSize, 0 )
        staticText.Wrap( -1 )
        holder.Add(staticText,1,wx.ALL|wx.ALIGN_CENTER|wx.EXPAND,5)

    def addTextCtrl(self,parent,holder,content=''):
        m_TCtrl= wx.TextCtrl( parent.GetStaticBox(), wx.ID_ANY, content, wx.DefaultPosition, wx.DefaultSize, 0 )
        m_TCtrl.SetMaxSize( wx.Size( -1,50 ) )
        holder.Add(m_TCtrl, 1, wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )

    def getControlInfoArea(self,label):
        sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, label ), wx.VERTICAL )
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        m_radioBox1Choices = [ u"Choice One", u"choice two",'Choice Three' ,'Choice Four','Choice Five' ]
        self.m_radioBox1 = wx.RadioBox( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Clean UP",
                wx.DefaultPosition, wx.DefaultSize, m_radioBox1Choices, 1, wx.RA_SPECIFY_COLS )
        self.m_radioBox1.SetSelection( 0 )
        bSizer2.Add( self.m_radioBox1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        sbSizer5.Add( bSizer2, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        return sbSizer5
        
          
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def CharacterEntered( self, event ):
        event.Skip()
    
    def FNEnterPressed( self, event ):
        event.Skip()
    


