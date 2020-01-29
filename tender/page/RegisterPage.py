import os
import winreg
import wx
import datetime

# This is how you pre-establish a file filter so that the dialog
# only shows the extension(s) you want it to.
wildcard = "Doc files (*.doc)|*.doc|"     \
           "Docx file (*.docx)|*.docx|" \
           "All files (*.*)|*.*"

REG_PATH_ID = 1000
REG_DOWN_ID = 1001
REG_SEL_ID = 1002
REG_UP_ID = 1003
PERSON_SEL_ID = 1004
PERSON_UP_ID = 1005

class RegisterPage(wx.Panel):
    def __init__(self, parent, panelId):
        super(RegisterPage, self).__init__(parent, id = panelId,pos=(5, 5), size=(1000, 1000))
        self.isUpRegFile = False
        self.isUpPersonFile = False
        font = wx.Font(14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)

        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                 r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
        deskPath = winreg.QueryValueEx(key, "Desktop")[0]

        wx.StaticText(self,label="1.下载签到表(默认下载到桌面)",pos=(20,20)).SetFont(font)
        self.downRegFileTextCtrl = wx.TextCtrl(self, -1, deskPath + "\签到表.doc", size=(400,30),pos=(50,70),style=wx.TE_READONLY)
        b = wx.Button(self, REG_PATH_ID, "选择路径", (460,70))
        self.Bind(wx.EVT_BUTTON, self.OnDownButton, b)
        b = wx.Button(self, REG_DOWN_ID, "下载文件", (560, 70))
        self.Bind(wx.EVT_BUTTON, self.downREGFileButton, b)


        wx.StaticText(self, label="2.上传签到表", pos=(20, 130)).SetFont(font)
        self.upRegFileTextCtrl = wx.TextCtrl(self, -1, "", size=(400,30),pos=(50,180),style=wx.TE_READONLY)
        b = wx.Button(self, REG_SEL_ID, "选择文件", (460,180))
        self.Bind(wx.EVT_BUTTON, self.OnSelectButton, b)
        b = wx.Button(self, REG_UP_ID, "上传文件", (560, 180))
        self.Bind(wx.EVT_BUTTON, self.upLoadFileButton, b)
        self.upState = wx.TextCtrl(self,-1,"上传状态：否",size=(200,30), pos=(50, 230),style=wx.TE_READONLY|wx.BORDER_NONE)
        self.upState.SetFont(font)
        self.upState.SetBackgroundColour("white")
        # print(self.BackgroundColour)
        # (240, 240, 240, 255)
        self.upTime = wx.TextCtrl(self,-1,"上传时间：",size=(300,30),pos=(300, 230),style=wx.TE_READONLY|wx.BORDER_NONE)
        self.upTime.SetFont(font)
        self.upTime.SetBackgroundColour("white")

        wx.StaticText(self, label="3.上传法人委托书", pos=(20, 280)).SetFont(font)
        self.upPersonFileTextCtrl = wx.TextCtrl(self, -1, "", size=(400, 30), pos=(50, 330), style=wx.TE_READONLY)
        b = wx.Button(self, PERSON_SEL_ID, "选择文件", (460,330))
        self.Bind(wx.EVT_BUTTON, self.OnSelectButton, b)
        b = wx.Button(self, PERSON_UP_ID, "上传文件", (560, 330))
        self.Bind(wx.EVT_BUTTON, self.upLoadFileButton, b)
        self.personState = wx.TextCtrl(self,-1,"上传状态：否",size=(200,30), pos=(50, 380),style=wx.TE_READONLY|wx.BORDER_NONE)
        self.personState.SetFont(font)
        self.personState.SetBackgroundColour("white")
        # print(self.BackgroundColour)
        # (240, 240, 240, 255)
        self.personTime = wx.TextCtrl(self,-1,"上传时间：",size=(300,30),pos=(300, 380),style=wx.TE_READONLY|wx.BORDER_NONE)
        self.personTime.SetFont(font)
        self.personTime.SetBackgroundColour("white")

    def OnSelectButton(self, evt):
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=os.getcwd(),
            defaultFile="",
            wildcard=wildcard,
            style=wx.FD_OPEN | wx.FD_MULTIPLE |
                  wx.FD_CHANGE_DIR | wx.FD_FILE_MUST_EXIST |
                  wx.FD_PREVIEW
        )

        # Show the dialog and retrieve the user response. If it is the OK response,
        # process the data.
        if dlg.ShowModal() == wx.ID_OK:
            # This returns a Python list of files that were selected.
            paths = dlg.GetPaths()
            for path in paths:
                if evt.GetId() == REG_SEL_ID:
                    self.upRegFileTextCtrl.SetValue(path)
                if evt.GetId() == PERSON_SEL_ID:
                    self.upPersonFileTextCtrl.SetValue(path)
        dlg.Destroy()


    def OnDownButton(self):
        print("CWD: %s\n" % os.getcwd())

        # Create the dialog. In this case the current directory is forced as the starting
        # directory for the dialog, and no default file name is forced. This can easilly
        # be changed in your program. This is an 'save' dialog.
        #
        # Unlike the 'open dialog' example found elsewhere, this example does NOT
        # force the current working directory to change if the user chooses a different
        # directory than the one initially set.
        dlg = wx.FileDialog(
            self, message="Save file as ...", defaultDir=os.getcwd(),
            defaultFile="", wildcard=wildcard, style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT
        )

        # This sets the default filter that the user will initially see. Otherwise,
        # the first filter in the list will be used by default.
        dlg.SetFilterIndex(2)

        # Show the dialog and retrieve the user response. If it is the OK response,
        # process the data.
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.downRegFileTextCtrl.SetValue(path)
            print('You selected "%s"' % path)

        # Note that the current working dir didn't change. This is good since
        # that's the way we set it up.
        print("CWD: %s\n" % os.getcwd())

        # Destroy the dialog. Don't do this until you are done with it!
        # BAD things can happen otherwise!
        dlg.Destroy()

    def upLoadFileButton(self,evt):
        infoStr = ""
        if evt.GetId() == REG_UP_ID:
            upPath = self.upRegFileTextCtrl.GetValue()
            if upPath == "":
                infoStr = u"未选择文件，无法上传"
            else:
                infoStr = u"文件上传成功\n" + upPath
                self.upState.SetValue("上传状态：是")
                self.upTime.SetValue("上传时间：" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                self.isUpRegFile = True
        if evt.GetId() == PERSON_UP_ID:
            upPath = self.upPersonFileTextCtrl.GetValue()
            if upPath == "":
                infoStr = u"未选择文件，无法上传"
            else:
                infoStr = u"文件上传成功\n" + upPath
                self.personState.SetValue("上传状态：是")
                self.personTime.SetValue("上传时间：" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                self.isUpPersonFile = True

        dlg = wx.MessageDialog(None, infoStr, u"提示信息", wx.OK | wx.ICON_INFORMATION)
        if dlg.ShowModal() == wx.ID_OK:
            dlg.Destroy()

    def downREGFileButton(self):
        downPath = self.downRegFileTextCtrl.GetValue()
        dlg = wx.MessageDialog(None, "签到表下载成功\n" + downPath, u"提示信息", wx.OK | wx.ICON_INFORMATION)
        if dlg.ShowModal() == wx.ID_OK:
            dlg.Destroy()
        print(downPath)

    def returnState(self):
        if self.isUpPersonFile and self.isUpRegFile:
            return True
        else:
            return False