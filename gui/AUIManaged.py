#!/usr/bin/env python3
import wx
import wx.lib.agw.aui as aui
from . import InfoInputPanel as IIP
from . import MeaningPanel as MP

class AUIManager( aui.AuiManager ) :
    """ AUI Manager class """

    def __init__( self, managed_window ) :
        """  """
        aui.AuiManager.__init__( self )
        self.SetManagedWindow( managed_window )
        
#end class

#------------------------------------------------------------------------------

class AUINotebook( aui.AuiNotebook ) :
    """ AUI Notebook class """

    def __init__( self, parent ) :
        """  """
        
        aui.AuiNotebook.__init__( self, parent=parent )
        
        self.default_style = aui.AUI_NB_DEFAULT_STYLE | aui.AUI_NB_TAB_EXTERNAL_MOVE | wx.NO_BORDER
        self.SetWindowStyleFlag( self.default_style )
        
        #----

        # add some pages to the notebook
        pages = [IIP.InfoInputPanel,MP.VocabPanel]

        pageCtr = 1
        for page in pages :
            label = 'Long tabnname and wrappable Tab #{}' .format(pageCtr)
            tab = page( self )
            self.AddPage( tab, label, False )
            pageCtr += 1
        #end for
    #end __init__

    def addPage(self,page):
        self.AddPage(page,"Test Label",False)
    
#end AUINotebook class

#------------------------------------------------------------------------------

class AuiManagedPanel(wx.Panel):
    ID_NotebookArtGloss     = wx.NewId()
    ID_NotebookArtSimple    = wx.NewId()
    ID_NotebookArtVC71      = wx.NewId()
    ID_NotebookArtFF2       = wx.NewId()
    ID_NotebookArtVC8       = wx.NewId()
    ID_NotebookArtChrome    = wx.NewId()
    
    #----------------------------------

    def __init__(self,parent):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, 
                size = wx.DefaultSize, style = wx.TAB_TRAVERSAL )
        self.aui_mgr = AUIManager(self)
        self.notebook = AUINotebook(self)
        self.notebook_style = self.notebook.default_style
        self.aui_mgr.AddPane(self.notebook,
                aui.AuiPaneInfo().Name("notebook_content").
                CenterPane().PaneBorder( False) )
        self.aui_mgr.Update()

    def OnChangeTabClose( self, event ) :
        """
        Change how the close button behaves on a tab
 
        Note : Based partially on the agw AUI demo
        """
        choice = event.GetString()
        self._notebook_style &= ~( aui.AUI_NB_CLOSE_BUTTON |
                                   aui.AUI_NB_CLOSE_ON_ACTIVE_TAB |
                                   aui.AUI_NB_CLOSE_ON_ALL_TABS )

        # note that this close button doesn't work for some reason
        if choice == "Close Button At Right" :
            self._notebook_style ^= aui.AUI_NB_CLOSE_BUTTON
            
        elif choice == "Close Button On All Tabs" :
            self._notebook_style ^= aui.AUI_NB_CLOSE_ON_ALL_TABS
            
        elif choice == "Close Button On Active Tab" :
            self._notebook_style ^= aui.AUI_NB_CLOSE_ON_ACTIVE_TAB

        self.notebook.SetWindowStyleFlag( self._notebook_style )
        self.notebook.Refresh()
        self.notebook.Update()
    
    #end OnChangeTabClose def
    
    #----------------------------------
    
    def OnChangeTheme( self, event ) :
        """
        Changes the notebook's theme
 
        Note : Based partially on the agw AUI demo
        """

        print( event.GetString())
        evId = self.themeDict[event.GetString()]
        print (evId)

        all_panes = self.aui_mgr.GetAllPanes()

        for pane in all_panes :

            if isinstance( pane.window, aui.AuiNotebook ) :
                nb = pane.window

                if evId == ID_NotebookArtGloss :

                    nb.SetArtProvider( aui.AuiDefaultTabArt() )
                    self._notebook_theme = 0

                elif evId == ID_NotebookArtSimple :
                    nb.SetArtProvider( aui.AuiSimpleTabArt() )
                    self._notebook_theme = 1

                elif evId == ID_NotebookArtVC71 :
                    nb.SetArtProvider( aui.VC71TabArt() )
                    self._notebook_theme = 2

                elif evId == ID_NotebookArtFF2 :
                    nb.SetArtProvider( aui.FF2TabArt() )
                    self._notebook_theme = 3

                elif evId == ID_NotebookArtVC8 :
                    nb.SetArtProvider( aui.VC8TabArt() )
                    self._notebook_theme = 4

                elif evId == ID_NotebookArtChrome :
                    nb.SetArtProvider( aui.ChromeTabArt() )
                    self._notebook_theme = 5

                #nb.SetWindowStyleFlag( self._notebook_style )
                nb.Refresh()
                nb.Update()
                
            #end if
            
        # end for
        
    #end OnChangeTheme def
    
    #----------------------------------
    
    def OnDisableTab( self, event ) :
        """ Disables the current tab. """
        
        page = self.notebook.GetCurrentPage()
        page_idx = self.notebook.GetPageIndex( page )

        self.notebook.EnableTab( page_idx, False )
        self.notebook.AdvanceSelection()

    #----------------------------------
