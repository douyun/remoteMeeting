import wx

class MeetStart(wx.Panel):
    def __init__(self, parent, panelId):
        super(MeetStart, self).__init__(parent, id = panelId,pos=(5, 5), size=(1000, 1000))
        self.state = False
        font = wx.Font(20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)

        wx.TextCtrl(self, -1, "    主持人宣布会议内容及纪律", size=(1000, 35), pos=(-2, -1), style=wx.TE_READONLY).SetFont(font)
        wx.TextCtrl(self, -1, """
        尊敬的各位领导及各投标企业代委，大家好！
        受（）凌托，（）代理并主持此次开标会议，现在会议开始。
        第一项，介绍参加会议的单位及人员，参加此次开标会的主要有：
        1、招标代理公司：（）2、投标单值：（）第二项、请（）讲话。
        第三项请（）室读会议纪律要求。
        第四项、宣布招标评标委员会人员超成情况。监督管理部门通过对课设单位及安麻市专家库相关专家运行感机抽取，组成5人评标委员会，其中业主代表1人，专家4人。
        第五项、宣布监督管理、等标、会议记录人员名单：
        1、监督管理（）2、哈标（）3、会议记录（）第六项、直布招标文件规定的评标、定标原则及办法。本工程采用综合评估法，具体评标办法请梦照招标文件。
        """, size=(796,500), pos=(0, 40),style=wx.TE_READONLY | wx.TE_MULTILINE)
        wx.TextCtrl(self,-1,"    情况备注",size=(1000,35), pos=(-2, 545),style=wx.TE_READONLY).SetFont(font)
        wx.TextCtrl(self, -1, """
        投标企业未在规定时间内签到，所以取消其参会资格
        """, size=(796,140), pos=(0, 585),style=wx.TE_READONLY | wx.TE_MULTILINE)

    def OnClick(self,evt):
        self.state = True

    def returnState(self):
        if self.state:
            return True
        else:
            return False