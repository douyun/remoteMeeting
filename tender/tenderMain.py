#!/usr/bin/env python

import wx
import wx.adv
from page import RegisterPage
from page import JoinMeeting
from page import  MeetStart
from page import  IdentifyCheck
#----------------------------------------------------------------------
# There are better ways to do IDs, but this demo requires that the window
# IDs be in a specific range. There are better ways to do that, too, but
# this will do for purposes of this demo.

ID_Menu_Exit        = 5005
ID_WINDOW_TOP       = 5000
ID_WINDOW_RIGHT     = 5001
ID_WINDOW_LEFT     = 5002
ID_WINDOW_BOTTOM    = 5003

#----------------------------------------------------------------------

class MyParentFrame(wx.MDIParentFrame):

    def __init__(self):
        wx.MDIParentFrame.__init__(
            self, None, -1, "汉滨区远程开标会议系统（代理企业端）", size=(1000,900),
            style = wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX
            )

        self.winCount = 0
        menu = wx.Menu()
        menu.Append(ID_Menu_Exit, "E&xit")

        menubar = wx.MenuBar()
        menubar.Append(menu, "&File")
        self.SetMenuBar(menubar)

        #self.CreateStatusBar()

        self.Bind(wx.EVT_MENU, self.OnExit, id=ID_Menu_Exit)
        self.Bind(wx.EVT_SIZE, self.OnSize)


        # Create some layout windows
        # A window like a toolbar
        win = wx.adv.SashLayoutWindow(self, ID_WINDOW_TOP, style=wx.NO_BORDER)
        win.SetDefaultSize((1000, 80))
        win.SetOrientation(wx.adv.LAYOUT_HORIZONTAL)
        win.SetAlignment(wx.adv.LAYOUT_TOP)
        win.SetBackgroundColour(wx.Colour(227, 238, 251))
        win.SetSashVisible(wx.adv.SASH_BOTTOM, False)

        font = wx.Font(24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        wx.StaticText(win, -1, "汉滨区远程开标会议系统（投标企业端）", (20, 10), (1000, -1), wx.ALIGN_CENTER).SetFont(font)

        wx.StaticLine(win, -1, pos=(2,45),size=(1000, -1), style=wx.LI_HORIZONTAL)
        font = wx.Font(16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        wx.StaticText(win, -1, "会议名称：大竹园镇危房改造项目", (20, 50)).SetFont(font)
        wx.StaticText(win, -1, "代理单位：万隆金建项目管理有限公司", (500, 50)).SetFont(font)

        self.topWindow = win


        # A window like a statusbar
        win = wx.adv.SashLayoutWindow(self, ID_WINDOW_BOTTOM, style=wx.NO_BORDER|wx.adv.SW_3D)
        win.SetDefaultSize((1000, 25))
        win.SetOrientation(wx.adv.LAYOUT_HORIZONTAL)
        win.SetAlignment(wx.adv.LAYOUT_BOTTOM)
        win.SetBackgroundColour(wx.Colour(227, 238, 251))
        win.SetSashVisible(wx.adv.SASH_TOP, False)
        wx.StaticText(win, -1, "版权所有©马豪工作室", (0, -1), (0, -1), wx.ALIGN_CENTER)
        self.bottomWindow = win


        # Another window to the left of the client window
        win = wx.adv.SashLayoutWindow(self, ID_WINDOW_LEFT, style=wx.NO_BORDER|wx.adv.SW_3D)
        win.SetDefaultSize((180, 1000))
        win.SetOrientation(wx.adv.LAYOUT_VERTICAL)
        win.SetAlignment(wx.adv.LAYOUT_LEFT)
        win.SetBackgroundColour(wx.Colour(100, 100, 120))
        win.SetSashVisible(wx.adv.SASH_RIGHT, False)

        pannel = wx.Panel(win)
        self.buttonStrList = ["会议签到","加入会议","会议开始","身份查验","投标文件下载","投标文件解密","技术标标准格式评审","宣布评审结果","商务标评审","投标函打印","唱标","招标人选择抽取k值企业","投标人代理抽取k、r值","确认唱标表","确认评审结果","宣布开标评审结果","对开标结果签宇","开标会议结束"]
        buLen = len(self.buttonStrList)
        for i in range(buLen):
            tem = self.buttonStrList[i]
            b = wx.Button(pannel, i, tem,(15,i*40+15),(150,30))
            self.Bind(wx.EVT_BUTTON, self.OnClick, b)
        self.leftWindow = win
        self.index = 0


        # Another window to the left of the client window
        win = wx.adv.SashLayoutWindow(self, ID_WINDOW_RIGHT, style=wx.NO_BORDER|wx.adv.SW_3D)
        win.SetDefaultSize((2000, 1000))
        win.SetOrientation(wx.adv.LAYOUT_VERTICAL)
        win.SetAlignment(wx.adv.LAYOUT_LEFT)
        win.SetBackgroundColour(wx.Colour(255, 255, 255))
        win.SetSashVisible(wx.adv.SASH_RIGHT, True)
        self.rightWindow = win
        self.mainPanel = None

    def OnClick(self, event):
        if event.GetId() == self.index:
            if event.GetId() == 0:
                self.mainPanel = RegisterPage.RegisterPage(self.rightWindow, -1)
                event.GetEventObject().Disable()
                self.index = 1
            elif event.GetId() == 1:
                if not self.mainPanel.returnState():
                    dlg = wx.MessageDialog(None, "没有完成会议签到，不能进行下一步", u"提示信息", wx.OK | wx.ICON_ERROR)
                    if dlg.ShowModal() == wx.ID_OK:
                        dlg.Destroy()
                else:
                    self.mainPanel.Destroy()
                    self.mainPanel = JoinMeeting.JoinMeeting(self.rightWindow,-1,123456)
                    event.GetEventObject().Disable()
                    self.index = 2
            elif event.GetId() == 2:
                if not self.mainPanel.returnState():
                    dlg = wx.MessageDialog(None, "没有打开远程会议软件，不能进行下一步", u"提示信息", wx.OK | wx.ICON_ERROR)
                    if dlg.ShowModal() == wx.ID_OK:
                        dlg.Destroy()
                else:
                    self.mainPanel.Destroy()
                    self.mainPanel = MeetStart.MeetStart(self.rightWindow, -1)
                    event.GetEventObject().Disable()
                    self.index = 3
            elif event.GetId() == 3:
                self.mainPanel.Destroy()
                self.mainPanel = IdentifyCheck.IdentifyCheck(self.rightWindow, -1)
                event.GetEventObject().Disable()
                self.index = 3
            else:
                p = wx.Panel(self.rightWindow, -1, size=(200, 500), pos=(30, 30))
                wx.StaticText(p, -1, "我是" + self.buttonStrList[event.GetId()] + "页面", (10, 10))
                self.mainPanel.Destroy()
                self.mainPanel = p
        else:
            dlg = wx.MessageDialog(None, "当前只能选择【" + self.buttonStrList[self.index] + "】，不能选择其他步骤", u"提示信息", wx.OK | wx.ICON_ERROR)
            if dlg.ShowModal() == wx.ID_OK:
                dlg.Destroy()
        # if event.GetId() == 3:
        #     self.mainPanel = IdentifyCheck.IdentifyCheck(self.rightWindow, -1)

    def OnSize(self, event):
        wx.adv.LayoutAlgorithm().LayoutMDIFrame(self)

    def OnExit(self, evt):
        self.Close(True)


#----------------------------------------------------------------------

if __name__ == '__main__':
    class MyApp(wx.App):
        def OnInit(self):
            frame = MyParentFrame()
            frame.Show(True)
            self.SetTopWindow(frame)
            return True

    app = MyApp(False)
    app.MainLoop()



