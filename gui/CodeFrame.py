#!/usr/bin/env python3

import wx
from wx import grid
from . import InfoInputPanel as IIP
from . import AUIManaged as AMP

class MainPanel(wx.Panel):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent = parent)

        self.txtOne = wx.StaticText(self, -1, label = "piradoba" )
        self.txtPlace = wx.TextCtrl(self, pos = (20,30))
        self.txtTwo = wx.StaticText(self, -1, label = "", pos = (20,40))

        button = wx.Button(self, label = "search", pos = (20,70))
        button.Bind(wx.EVT_BUTTON, self.onButton)

    def onButton(self, event):
        var=self.txtPlace.GetValue()
        if len(var) == 9 or len(var) == 11:
            print ("???")
        # MainPanel->SplitterWindow->MainFrame ( 2x GetParent() )
        self.GetParent().GetParent().AddPanel()

class SecondPanel(wx.Panel):

    def __init__(self, parent,a,b):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)

        MyGrid=grid.Grid(self)
        MyGrid.CreateGrid(a, b)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(MyGrid, 0, wx.EXPAND)
        self.SetSizer(sizer)

class CodeFrame(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Dynamic Window Test", size=wx.DefaultSize)

        self.splitter = wx.SplitterWindow(self)

        self.panelOne = MainPanel(self.splitter)
        self.panelTwo = AMP.AuiManagedPanel(self.splitter)

        self.splitter.SplitHorizontally(self.panelOne, self.panelTwo)
        self.splitter.SetMinimumPaneSize(100)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.splitter, 2, wx.EXPAND)

        #self.PanelThree = IIP.InfoInputPanel(self)
        #self.sizer.Add(self.PanelThree,2,wx.EXPAND)

        self.SetSizer(self.sizer)

    def AddPanel(self):
        self.newPanel = SecondPanel(self, 1, 1)
        self.sizer.Add(self.newPanel, 1, wx.EXPAND)
        self.sizer.Layout()
    

