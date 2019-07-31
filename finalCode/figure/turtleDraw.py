# -*- coding:utf-8 -*-
import wx
import turtle


class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent=None,
                         title="Lyn's Tool",
                         size=(600, 200),
                         pos=(200, 300))  # 生成框架窗口
        panel = wx.Panel(frame, -1)
        self.buttonWJX = wx.Button(panel,
                                   -1,
                                   "五角星",
                                   size=(75, 25),
                                   pos=(10, 100))
        self.Bind(wx.EVT_BUTTON, self.OnButtonWJX, self.buttonWJX)

        self.buttonSJX = wx.Button(panel,
                                   -1,
                                   "三角星",
                                   size=(75, 25),
                                   pos=(90, 100))
        self.Bind(wx.EVT_BUTTON, self.OnButtonSJX, self.buttonSJX)

        self.buttonZFX = wx.Button(panel,
                                   -1,
                                   "正方形",
                                   size=(75, 25),
                                   pos=(170, 100))
        self.Bind(wx.EVT_BUTTON, self.OnButtonZFX, self.buttonZFX)

        self.buttonTX = wx.Button(panel,
                                  -1,
                                  "梯形",
                                  size=(75, 25),
                                  pos=(250, 100))
        self.Bind(wx.EVT_BUTTON, self.OnButtonTX, self.buttonTX)

        self.buttonYX = wx.Button(panel,
                                  -1,
                                  "圆形",
                                  size=(75, 25),
                                  pos=(330, 100))
        self.Bind(wx.EVT_BUTTON, self.OnButtonYX, self.buttonYX)

        self.buttonDBX = wx.Button(panel,
                                   -1,
                                   "多边形",
                                   size=(75, 25),
                                   pos=(410, 100))
        self.Bind(wx.EVT_BUTTON, self.OnButtonDBX, self.buttonDBX)

        self.buttonTYX = wx.Button(panel,
                                   -1,
                                   "椭圆形",
                                   size=(75, 25),
                                   pos=(490, 100))
        self.Bind(wx.EVT_BUTTON, self.OnButtonTYX, self.buttonTYX)
        self.buttonDX = wx.Button(panel,
                                   -1,
                                   "点形",
                                   size=(75, 25),
                                   pos=(570, 100))
        self.Bind(wx.EVT_BUTTON, self.OnButtonDX, self.buttonDX)

        frame.Show(True)  # 显示框架窗口
        return True

    ####注意，海龟笔头一开始默认是在直角坐标系的（0，0）位置

    def OnButtonWJX(self, event):  # 五角星
        turtle.pu()  # 抬起笔头
        turtle.hideturtle()  # 隐藏笔头，使得在移动时不可见
        turtle.goto(0, 0)  # 向前走到（x,y）位置
        turtle.pd()  # 放下笔头
        # turtle.showturtle()  # 显示笔头，开始绘图
        for i in range(5):
            turtle.forward(150)
            turtle.right(144)
        turtle.pu()
        turtle.goto(10,20)
        turtle.pd()
        turtle.dot()
        turtle.pu()
        turtle.goto(20,20)
        turtle.pd()
        turtle.dot()
        turtle.pu()
        turtle.goto(20,30)
        turtle.pd()
        turtle.dot()


    def OnButtonSJX(self, event):  # 三角形
        turtle.pu()
        turtle.hideturtle()
        turtle.goto(-100, 250)
        turtle.pd()
        turtle.showturtle()
        for i in range(3):
            turtle.forward(150)
            turtle.right(120)

    def OnButtonZFX(self, event):  # 正方形
        turtle.pu()
        turtle.hideturtle()
        turtle.goto(100, 250)
        turtle.showturtle()
        turtle.pd()
        for i in range(4):
            turtle.forward(150)
            turtle.right(90)

    def OnButtonTX(self, event):  # 梯形
        turtle.pu()
        turtle.hideturtle()
        turtle.goto(-230, 0)
        turtle.showturtle()
        turtle.pd()
        turtle.forward(100)
        turtle.right(30)
        turtle.forward(100)
        turtle.right(150)
        turtle.forward(274)
        turtle.right(150)
        turtle.forward(100)

    def OnButtonYX(self, event):  # 圆形
        turtle.pu()
        turtle.hideturtle()
        turtle.goto(0, 0)
        turtle.showturtle()
        turtle.pd()
        for i in range(36):
            turtle.forward(10)
            turtle.right(10)

    def OnButtonDBX(self, event):  # 多边形
        turtle.pu()
        turtle.hideturtle()
        turtle.goto(150, 0)
        turtle.showturtle()
        turtle.pd()
        for i in range(9):
            turtle.forward(40)
            turtle.right(40)

    def OnButtonTYX(self, event):  # 椭圆
        turtle.pu()
        turtle.hideturtle()
        turtle.goto(-250, -100)
        turtle.showturtle()
        turtle.pd()
        for i in range(10):
            turtle.forward(20)
            turtle.right(9)
        for i in range(10):
            turtle.forward(10)
            turtle.right(9)
        for i in range(10):
            turtle.forward(20)
            turtle.right(9)
        for i in range(10):
            turtle.forward(10)
            turtle.right(9)
    def OnButtonDX(self, event):
        turtle.pu()
        turtle.hideturtle()
        turtle.goto(0, 0)
        # turtle.showturtle()
        turtle.pd()
        for i in range(4):
            turtle.forward(150)
            turtle.left(90)
        turtle.pu()
        turtle.goto(10,20)
        turtle.pd()
        turtle.dot()
        turtle.pu()
        turtle.goto(20,40)
        turtle.pd()
        turtle.dot()
        turtle.pu()
        turtle.goto(40,60)
        turtle.pd()
        turtle.dot()

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()  # 进入消息循环
