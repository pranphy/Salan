#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import wx
import wx.xrc

class InfoInputPanel ( wx.Panel ):
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, 
                size = wx.DefaultSize, style = wx.TAB_TRAVERSAL )
        
        OutermostGBSizer = wx.GridBagSizer( 0, 0 )
        OutermostGBSizer.SetFlexibleDirection( wx.BOTH )
        OutermostGBSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        OutermostGBSizer.Add( self.getInputInfoArea( _('Input Informations')),
                wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
     
        OutermostGBSizer.Add( self.getControlInfoArea(_('Control Area')),
                wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
        
        OutermostGBSizer.AddGrowableCol( 0 )
        OutermostGBSizer.AddGrowableCol( 1 )
        OutermostGBSizer.AddGrowableRow( 0 )
        
        self.SetSizer( OutermostGBSizer )
        self.Layout()
 
    def getInputInfoArea(self,label):
        InputsSBSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, label ), wx.VERTICAL )
        
        CellsFGSizer = wx.FlexGridSizer( 0, 2, 0, 0 )

        CellsFGSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        input_list = [_('Hello World'),_('Last Name'),_('Home Address'),_('Email Address')]

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
        TCtrl= wx.TextCtrl( parent.GetStaticBox(), wx.ID_ANY, content, wx.DefaultPosition, wx.DefaultSize, 0 )
        TCtrl.SetMaxSize( wx.Size( -1,50 ) )
        holder.Add(TCtrl, 1, wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )

    def getControlInfoArea(self,label):
        sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, label ), wx.VERTICAL )
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        radioBox1Choices = [ _('Choice One'), _('choice two'),_('Choice Three') ,_('Choice Four'),_('Choice Five') ]
        self.radioBox1 = wx.RadioBox( sbSizer5.GetStaticBox(), wx.ID_ANY, _('Clean UP'),
                wx.DefaultPosition, wx.DefaultSize, radioBox1Choices, 1, wx.RA_SPECIFY_COLS )
        self.radioBox1.SetSelection( 0 )
        bSizer2.Add( self.radioBox1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        sbSizer5.Add( bSizer2, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        return sbSizer5
        
          
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def CharacterEntered( self, event ):
        event.Skip()
    
    def FNEnterPressed( self, event ):
        event.Skip()
    


