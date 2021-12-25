import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="1")
        self.SetSize(300, 170)
        self.mainPanel = wx.Panel(self)
        self.upperPanel = wx.Panel(self.mainPanel)

        self.upgridSizer=wx.GridSizer(rows=1,cols=1,hgap=4,vgap=4)
        self.bincan = wx.TextCtrl(self.upperPanel,value='0')
        self.upgridSizer.Add(self.bincan,1,wx.EXPAND)

        self.hzBoxSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.hzBoxSizer.Add(self.upgridSizer,1,wx.EXPAND,5)
        self.upperPanel.SetSizer(self.hzBoxSizer)

        self.gridSizer = wx.GridSizer(rows = 4, cols=5, hgap=5, vgap=5)
        
        self.buttons = (
            wx.Button(self.mainPanel, label="7"),
            wx.Button(self.mainPanel, label="8"),
            wx.Button(self.mainPanel, label="9"),
            wx.Button(self.mainPanel, label="/"),
            wx.Button(self.mainPanel, label="C"),
            wx.Button(self.mainPanel, label="4"),
            wx.Button(self.mainPanel, label="5"),
            wx.Button(self.mainPanel, label="6"),
            wx.Button(self.mainPanel, label="*"),
            wx.Button(self.mainPanel, label="BS"),
            wx.Button(self.mainPanel, label="1"),
            wx.Button(self.mainPanel, label="2"),
            wx.Button(self.mainPanel, label="3"),
            wx.Button(self.mainPanel, label="-"),
            wx.Button(self.mainPanel, label="±"),
            wx.Button(self.mainPanel, label="0"),
            wx.Button(self.mainPanel, label="."),
            wx.Button(self.mainPanel, label="="),
            wx.Button(self.mainPanel, label="+"),
            wx.Button(self.mainPanel, label="CE"),
            )
                           
        for button in self.buttons:
            self.gridSizer.Add(button, 0, wx.EXPAND)

        self.vtBoxSizer = wx.BoxSizer(wx.VERTICAL)
        self.vtBoxSizer.Add(self.upperPanel, 0, wx.EXPAND | wx.TOP, 15)
        self.vtBoxSizer.Add(self.gridSizer, 1, wx.EXPAND, 5)
        self.mainPanel.SetSizer(self.vtBoxSizer)

app = wx.App()
frame = MyFrame()
frame.Show()
app.MainLoop()
