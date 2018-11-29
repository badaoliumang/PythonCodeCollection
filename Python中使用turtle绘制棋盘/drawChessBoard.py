import turtle
#声明棋盘的单元格宽度为30，数量为18
width = 30
num = 18
#设置画布大小
turtle.screensize(1200,900,"green")
#声明列表来存取坐标
x1 = [(-400,400),(-400+width*num,400)]
y1 = [(-400,400),(-400,400-width*num)]
#获取画笔
t = turtle.Pen()
#设置画笔速度(1-10)越大速度越快
t.speed(8)
#设置画笔颜色
t.pencolor("red")

#循环绘制横向线
for i in range(0,19):
    t.penup()
    t.goto(x1[0][0],x1[0][1]-30*i)
    t.pendown()
    t.goto(x1[1][0],x1[1][1]-30*i)
#循环绘制纵向线
for i in range(0,19):
    t.penup()
    t.goto(y1[0][0]+30*i,y1[0][1])
    t.pendown()
    t.goto(y1[1][0]+30*i,y1[1][1])

#隐藏画笔
t.hideturtle()
#保证运行窗口不被关闭
turtle.done()
