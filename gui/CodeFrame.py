#!/usr/bin/env python3

import wx
from . import AUIManaged as AMP

class CodeFrame(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Dynamic Window Test", size=wx.DefaultSize)

        self.MainPanel= AMP.AuiManagedPanel(self)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.MainPanel, 2, wx.EXPAND)

        self.SetSizer(self.sizer)
