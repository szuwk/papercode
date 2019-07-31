# -*- coding:utf-8 -*-
from turtle import Screen,Turtle
import turtle
import time
import pandas as pd
data = pd.read_csv(r'E:\paperData\allData\newmk_329.txt', sep='\t')
data = data[(data.A5 ==3) & (data.trans_pattern==8)]
# data = data[data.A5 ==3]
data.to_csv(r'dt.txt',sep = '\t',index=False)
data =pd.read_csv(r'dt.txt',sep = '\t')
# data = data1[data1.X!=0]

def OnButtondxt(data):
        turtle.pu()
        turtle.hideturtle()
        turtle.goto(0, 0)
        # turtle.showturtle()
        turtle.pd()
        for i in range(4):
            turtle.forward(525)
            turtle.left(90)
        for i in range(int(len(data)/100)):
        # for i in range(500):
            print(i,int(data['X'][i]),data['trans_pattern'][i])
            X = int(data['X'][i])
            Y = int(data['Y'][i])
            turtle.speed(3)
            turtle.pu()
            turtle.goto(X, Y)
            turtle.pd()
            turtle.dot()
            # writer = Turtle()
            # writer.speed(0)
            # writer.hideturtle()
            # writer.up()
            # writer.goto(-20,20)
            # writer.write(i,font=(80))
            # time.sleep(0.1)
            # writer.undo()
        time.sleep(100)
    # ts = turtle.getscreen()
    # ts.getcanvas().postscript(file="work.jpg")
    # turtle.showturtle()
data1 = pd.read_csv(r'E:wallline.csv',sep = ',')
def drawPic(data,data1):
    turtle.pu()
    turtle.hideturtle()
    turtle.goto(-100, -100)
    # turtle.showturtle()
    turtle.pd()
    for i in range(4):
        turtle.forward(525)
        turtle.left(90)
    for i in range(len(data)):
        # for i in range(500):
        # print(i, int(data[''][i]), data['trans_pattern'][i])
        x1,y1=data['x1'][i]*10-100,data['y1'][i]*10-100
        x2, y2 = data['x2'][i]*10-100, data['y2'][i]*10-100
        turtle.speed(0)
        turtle.pu()
        turtle.goto(x1, y1)
        turtle.pd()
        turtle.goto(x2, y2)
        # writer = Turtle()
        # writer.speed(0)
        # writer.hideturtle()
        # writer.up()
        # writer.goto(-20,20)
        # writer.write(i,font=(80))
        # time.sleep(0.1)
        # writer.undo()
    for i in range(int(len(data1))):
        # for i in range(500):
        print(i, int(data1['X'][i]), data1['trans_pattern'][i])
        X = int(data1['X'][i])-100
        Y = 525-int(data1['Y'][i])-100
        turtle.speed(0)
        turtle.pu()
        turtle.goto(X, Y)
        turtle.pd()
        turtle.dot()
        # writer = Turtle()
        # writer.speed(0)
        # writer.hideturtle()
        # writer.up()
        # writer.goto(-20,20)
        # writer.write(i,font=(80))
        # time.sleep(0.1)
        # writer.undo()
    time.sleep(100)
    time.sleep(100)

# print(data)
if __name__ == "__main__":
    # app = MyApp()
    # app.MainLoop()  # 进入消息循环
    # OnButtondxt(data)
    drawPic(data1,data)