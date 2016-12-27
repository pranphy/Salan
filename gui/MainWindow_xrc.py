#!/usr/bin/env python3
import wx
from wx import xrc
from srv import WordSrv as ws


class VMainWindow(wx.Frame):
    def __init__(self,parent=None):
        #super.__init__(wx.Frame,parent)
        self.is_xrc_read = False
        self.read_xrc()

    def Show(self):
        self.Frame.Show(True)

    def read_xrc(self):
        self.res = xrc.XmlResource('./res/xrc/SecondFrame.xrc')
        self.Frame = self.res.LoadFrame(None, 'NewFrame')
        self.is_xrc_read = True
        self.bind_events()

    def bind_events(self):
        self.ButtonOne = xrc.XRCCTRL(self.Frame, 'ID_FirstButton')
        self.MeaningText = xrc.XRCCTRL(self.Frame,'ID_MeaningSText')
        self.EnteredWord = xrc.XRCCTRL(self.Frame,'ID_WordInputTCtrl')
        
        #Bind Functions Below
        self.Frame.Bind(wx.EVT_BUTTON,self.OnButtonOneClick,self.ButtonOne)
        self.Frame.Bind(wx.EVT_TEXT_ENTER,self.OnTextEnterPressed,self.EnteredWord)

    def OnTextEnterPressed(self,evt):
        self.OnButtonOneClick(evt)

    def OnButtonOneClick(self,evt):
        word = self.EnteredWord.GetLineText(0)
        self.MeaningText.SetLabel('searching meaning for {}'.format(word))
        a = ws.WordSrv(word)
        meaning = a.get_short_def()
        self.MeaningText.SetLabel(str(meaning))

    def HistOnButtonOneClick(self,evt):
        openFileDialog = wx.FileDialog(
            self.Frame,
            "Open Image file", "", "",
            "JPG files (*.jpg)|*.jpg",
            wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
        )
        if openFileDialog.ShowModal() == wx.ID_CANCEL:
            return     # the user changed idea...

        # proceed loading the file chosen by the user
        # this can be done with e.g. wxPython input streams:
        input_stream = wx.FileInputStream(openFileDialog.GetPath())
        if not input_stream.IsOk():
            wx.LogError("Cannot open file '%s'."%openFileDialog.GetPath())
            return

class VcMainWindow(VMainWindow().Frame):
    def __init__():
        pass


