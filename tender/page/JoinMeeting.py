import os
import wx
from page import images

class JoinMeeting(wx.Panel):
    def __init__(self, parent, panelId,meetid):
        super(JoinMeeting, self).__init__(parent, id = panelId,pos=(5, 5), size=(1000, 1000))
        self.state = False
        font = wx.Font(20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)

        wx.TextCtrl(self, -1, "    会议账号获取", size=(1000, 35), pos=(-2, -1), style=wx.TE_READONLY).SetFont(font)
        wx.StaticText(self,label="会议账号",pos=(50,100)).SetFont(font)
        self.meetTextCtrl = wx.TextCtrl(self, -1, str(meetid), size=(400,30),pos=(200,100),style=wx.TE_READONLY|wx.TE_CENTER)
        self.meetTextCtrl.SetBackgroundColour("white")
        self.meetTextCtrl.SetFont(font)

        wx.TextCtrl(self,-1,"    远程会议系统登录",size=(1000,35), pos=(-2, 230),style=wx.TE_READONLY).SetFont(font)

        font = wx.Font(16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        b = wx.Button(self, 50, " 点击登录",size=(170,50) , pos=(50, 350))
        b.SetFont(font)
        b.SetToolTip("点击此按钮打开远程会议视频系统")
        self.Bind(wx.EVT_BUTTON, self.OnClick, b)
        # imgPath =  os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/img/111.png"
        # images = wx.Bitmap(imgPath, wx.BITMAP_TYPE_PNG)
        bmp = images.icon.GetBitmap()
        b.SetBitmap(bmp,
                    wx.LEFT    # Left is the default, the image can be on the other sides too
                    #wx.RIGHT
                    #wx.TOP
                    #wx.BOTTOM
                    )
        # b.SetBitmapMargins((2,2)) # default is 4 but that seems too big to me.

    def OnClick(self,evt):
        # cmdstr = "D:\\03_python\\01_wxPython\\02_practice\\dist\\111.exe"
        # # os.system(cmdstr)
        # os.startfile(cmdstr)
        self.state = True

    def returnState(self):
        if self.state:
            return True
        else:
            return False