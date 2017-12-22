import wx
from wx import xrc
class PhonePanelHandler(xrc.XmlResourceHandler):
    def CanHandle(self,node):
        return self.IsOfClass(node,"PhoneButtonPanel")

    def DoCreateResource(self):
        panel = PhoneButtonPanel(self.GetParentAsWindow())
        self.SetupWindow(panel)
        self.CreateChildren(panel)
        return panel

class CustomXmlResource(xrc.XmlResource):
    def __init__(self,fileName):
        super(CustomXmlResource,self).__init__(fileName)

        self.InsertHandler(PhonePanelHandler())
