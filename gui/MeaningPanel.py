#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import wx
import wx.richtext as rt
import wx.xrc
from srv import GeneralServices as gs
from srv import WordSrv as ws

class VocabPanel ( wx.Panel ):
    
    def __init__( self, parent ):
        wx.Panel.__init__(self, parent,id = wx.ID_ANY,pos = wx.DefaultPosition,
                size = wx.DefaultSize, style = wx.TAB_TRAVERSAL )
        
        VPanelBSizer = wx.BoxSizer( wx.VERTICAL )
        VPanelBSizer.Add( self.createInputWordArea(), 1, wx.EXPAND, 5 )
        VPanelBSizer.Add( self.createDetailArea(), 5, wx.EXPAND, 5 )
        self.InputWordTCtrl.Bind( wx.EVT_TEXT_ENTER, self.OnEnterPressed ) 
        self.SetSizer( VPanelBSizer )
        self.Layout()


    def createInputWordArea(self,label="Input Word"):
        IpWordSBSIzer = wx.StaticBoxSizer( 
                wx.StaticBox( self, wx.ID_ANY, label ), wx.VERTICAL )
        WIRowBSizer = wx.BoxSizer( wx.VERTICAL )

        self.InputWordTCtrl =  self.createTextCtrl(IpWordSBSIzer)
        WIRowBSizer.Add(self.InputWordTCtrl, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
        
        self.SearchButton = wx.Button( IpWordSBSIzer.GetStaticBox(), wx.ID_ANY, 
                u"Search Meaning", wx.DefaultPosition, wx.DefaultSize, 0 )
        WIRowBSizer.Add( self.SearchButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        IpWordSBSIzer.Add( WIRowBSizer, 1, wx.EXPAND, 5 )

        return IpWordSBSIzer
        
        
    def createDetailArea(self,label="Fetched Detail"): 
        self.FDetailSBSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, label ), wx.VERTICAL )
        self.DRowsFGSizer = wx.FlexGridSizer( 8, 2, 0, 0 )
        self.DRowsFGSizer.AddGrowableCol( 1 )
        self.DRowsFGSizer.SetFlexibleDirection( wx.BOTH )
        self.DRowsFGSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        InfoDict = {'meaning':_('Meaning'),
                'short_def':_('Short Definition'),
                'long_def':_('Long Definition'),
        }
        self.DetailDict = {}
        for code,label in InfoDict.items():
            FieldSText =  self.createStaticText(self.FDetailSBSizer,label)
            FieldSText.Wrap( -1 )
            self.DRowsFGSizer.Add( FieldSText, 2, wx.ALL, 5 )
            FieldTCtrl = self.createRichTextCtrl(self.FDetailSBSizer)
            self.DRowsFGSizer.Add(FieldTCtrl, 7, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
            self.DetailDict[code] = FieldTCtrl

        self.FDetailSBSizer.Add( self.DRowsFGSizer, 1, wx.EXPAND, 5 )
        return self.FDetailSBSizer

    def addSentences(self,word_srv):
        for sentence in word_srv.getSentences():
            FieldSText = self.createStaticText(self.FDetailSBSizer,label="Sentence ")
            FieldSText.Wrap(-1)
            self.DRowsFGSizer.Add( FieldSText, 2, wx.ALL, 5 )
            print(' {}  ::: is the sentence '.format(sentence))
            TextCtrl = self.createRichTextCtrl(self.FDetailSBSizer)
            self.DRowsFGSizer.Add(TextCtrl, 7, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
            TextCtrl.SetValue(sentence)

        self.Layout()


    def OnEnterPressed(self,event):
        RequestedWord = self.InputWordTCtrl.GetValue()
        self.DetailDict['meaning'].SetValue('Searching in the internet')
        word_srv = ws.WordSrv(RequestedWord)
        print('Received info from internet')
        meaning  = word_srv.getMeaning()
        print('Received info from internet')
        self.DetailDict['meaning'].SetValue(meaning)
        self.DetailDict['short_def'].SetValue(word_srv.get_short_def())
        self.DetailDict['long_def'].SetValue(word_srv.getLongDef())

        self.addSentences(word_srv)

    def createRichTextCtrl(self,parent):
        TextCtrl = rt.RichTextCtrl( parent.GetStaticBox(), id=wx.ID_ANY, 
                value=wx.EmptyString, pos=wx.DefaultPosition, 
                size=(-1,80),style=wx.richtext.RE_MULTILINE|wx.VSCROLL|wx.HSCROLL)
        return TextCtrl

    def createTextCtrl(self,parent):
        TextCtrl = wx.TextCtrl( parent.GetStaticBox(), id=wx.ID_ANY, 
                value=wx.EmptyString, pos=wx.DefaultPosition, 
                size=wx.DefaultSize,style=wx.TE_PROCESS_ENTER)
        return TextCtrl


    def createStaticText(self,parent,label='Static Label'):
        StaticText = wx.StaticText( parent.GetStaticBox(), wx.ID_ANY,
                label, wx.DefaultPosition, wx.DefaultSize, 0 )
        return StaticText

    def __del__( self ):
        pass
    
