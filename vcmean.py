#!/usr/bin/env python3

import wx
from wx import xrc

from vc import FetchMeaning as fm
from srv import WordSrv as ws
from srv import GeneralServices as ws
from gui import CodeFrame as cf


class MyApp(wx.App):
    def OnInit(self):
        ws.setLocale('ne_NP')
        self.MainWindow = cf.CodeFrame()
        self.MainWindow.Show()
        return True
    
if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()
