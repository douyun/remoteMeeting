import wx
from page import images

class IdentifyCheck(wx.Panel):
    def __init__(self, parent, panelId):
        super(IdentifyCheck , self).__init__(parent, id = panelId,pos=(5, 5), size=(1000, 1000))
        font = wx.Font(20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)

        wx.TextCtrl(self, -1, "    投标企业身份查验", size=(1000, 35), pos=(-2, -1), style=wx.TE_READONLY).SetFont(font)
        wx.StaticBox(self,-1,"",size=(780,500),pos=(10,50))
        wx.StaticText(self, label="""
请配合进行身份查验。请在主持人指引下手持身份证或者其他

有效证件对准摄像头配合拍照。具体参照下图。
        """, pos=(30, 70)).SetFont(font)

        # imgPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/img/idCheck.jpg"
        # images = wx.Bitmap(imgPath, wx.BITMAP_TYPE_JPEG)
        bmp = images.idcheck.GetBitmap()
        wx.StaticBitmap(self, -1, bmp, (250, 250))