import tkinter
import platform
from   cefpython3 import cefpython as cef
# Platforms
WINDOWS = (platform.system() == "Windows")
LINUX = (platform.system() == "Linux")
MAC = (platform.system() == "Darwin")
cef.Initialize()
class   Webbrowser:
    def __init__(self):
        self.URL = "http://www.baidu.com"
        self.WebFrame = None
    #设置URL
    def set_URL(self,url):
        self.URL = url
    #设置Canvas
    def set_Canvas(self,canvas):
        self.WebFrame = tkinter.ttk.Frame(canvas)
        W = canvas.winfo_width()
        H = canvas.winfo_height()
        self.WebFrame.place(x=0,y=0,width=W,height=H)
        self.navigation_bar = None
        self.closing = False
        self.browser = None
        self.WebFrame.bind("<FocusIn>", self.on_focus_in)
        self.WebFrame.bind("<FocusOut>", self.on_focus_out)
        self.WebFrame.bind("<Configure>", self.on_configure)
        self.WebFrame.focus_set()

    #查询
    def embed_browser(self,width,heith):
        window_info = cef.WindowInfo()
        rect = [0, 0, width, heith]
        window_info.SetAsChild(self.get_window_handle(), rect)
        self.browser = cef.CreateBrowserSync(window_info,url=self.URL) #todo
        assert self.browser
        self.message_loop_work()
        

    def get_window_handle(self):
        if self.WebFrame.winfo_id() > 0:
            return self.WebFrame.winfo_id()
        elif MAC:
            # On Mac window id is an invalid negative value (Issue #308).
            # This is kind of a dirty hack to get window handle using
            # PyObjC package. If you change structure of windows then you
            # need to do modifications here as well.
            # noinspection PyUnresolvedReferences
            from AppKit import NSApp
            # noinspection PyUnresolvedReferences
            import objc
            # Sometimes there is more than one window, when application
            # didn't close cleanly last time Python displays an NSAlert
            # window asking whether to Reopen that window.
            # noinspection PyUnresolvedReferences
            return objc.pyobjc_id(NSApp.windows()[-1].contentView())
        else:
            raise Exception("Couldn't obtain window handle")

    def message_loop_work(self):
        cef.MessageLoopWork()
        self.WebFrame.after(10, self.message_loop_work)

    def on_configure(self,event):
        print("on_configure")
        if not self.browser:
            print("embed_browser")
            self.embed_browser(event.width,event.height)
        else:
            print("on_mainframe_configure")
            self.on_mainframe_configure(event.width,event.height)

    def on_root_configure(self):
        # Root <Configure> event will be called when top window is moved
        if self.browser:
            self.browser.NotifyMoveOrResizeStarted()

    def on_mainframe_configure(self, width, height):
        if self.browser:
            if WINDOWS:
                ctypes.windll.user32.SetWindowPos(
                    self.browser.GetWindowHandle(), 0,
                    0, 0, width, height, 0x0002)
            elif LINUX:
                self.browser.SetBounds(0, 0, width, height)
            self.browser.NotifyMoveOrResizeStarted()

    def on_focus_in(self, _):
        if self.browser:
            self.browser.SetFocus(True)

    def on_focus_out(self, _):
        if self.browser:
            self.browser.SetFocus(False)

    def on_root_close(self):
        if self.browser:
            self.browser.CloseBrowser(True)
            self.clear_browser_references()
        self.WebFrame.destroy()
        cef.Shutdown()

    def clear_browser_references(self):
        # Clear browser references that you keep anywhere in your
        # code. All references must be cleared for CEF to shutdown cleanly.
        self.browser = None
