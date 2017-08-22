#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
import pymysql
from PIL import Image, ImageTk



#鼠标进出提交标签
def labelSubmitEnter(event):
    event.widget.config(bg = '#06A1E0')
def labelSubmitLeave(event):
    event.widget.config(bg = '#235DA9')

#登录验证
def labelSubmitClick(event):
    labelReminder.place(x=-500,y=560)
    event.widget.config(text = '正在登录')
    username = str(en.get())
    password = ((str(ep.get()),),)
    db = pymysql.connect(host = "localhost", user = "dan", password = "3224", db = "broadcastdb", port = 3306)
    cursor = db.cursor()
    cursor.execute('select psw from user where name = "%s"' % username)
    truepassword = cursor.fetchall()
    if truepassword == password:
        print('right')
    else:
        labelReminder.place(x=67,y=560)
        event.widget.config(text = '登  录')
    print(truepassword == password)
    print(truepassword)
    print(password)
    db.close()

#用户名输入框得到/失去焦点
def entryNameFocusIn(event):
    if en.get() == '请输入用户名':
        en.set('')

def entryNameFocusOut(event):
    if en.get() == '':
        en.set('请输入用户名')

#密码输入框得到/失去焦点
def entryPswFocusIn(event):
    if ep.get() == '请输入密码':
        event.widget.config(show = '*')
        ep.set('')

def entryPswFocusOut(event):
    if ep.get() == '':
        event.widget.config(show = '')
        ep.set('请输入密码')

        

#建立tkinter窗口，设置标题

login = tk.Tk()
login.title('Login')
login.geometry('450x700')
login.resizable(width = False, height = False)


#放置背景图
canvas = tk.Canvas(login, width = 450, height = 700)
image = Image.open('loginbg.jpg')
im = ImageTk.PhotoImage(image)

canvas.create_image(450/2,700/2,image = im)
canvas.place(x=0,y=0)


###窗口中添加标题标签
##labelTitle = tk.Label(login, text = '青阳广播电视台\n广播播出系统', fg = '#235DA9', font = ('微软雅黑', 36), height = 5)
##labelTitle.pack()

#窗口中添加用户名输入框
en = tk.StringVar()
entryName = tk.Entry(login, textvariable = en, font = ('微软雅黑', 33), width = 12, fg = 'gray', relief = 'flat')
en.set('请输入用户名')
entryName.place(x=67,y=350)
#entryName.pack(side = 'bottom')
#得到/失去焦点
entryName.bind('<FocusIn>', entryNameFocusIn)
entryName.bind('<FocusOut>', entryNameFocusOut)

#窗口中添加密码输入框
ep = tk.StringVar()
entryPsw = tk.Entry(login, textvariable = ep, font = ('微软雅黑', 33), width = 12, fg = 'gray', relief = 'flat')
ep.set('请输入密码')
entryPsw.place(x=67,y=420)
#得到/失去焦点
entryPsw.bind('<FocusIn>', entryPswFocusIn)
entryPsw.bind('<FocusOut>', entryPswFocusOut)

#窗口中添加提交按钮
labelSubmit = tk.Label(login, text = '登  录', font = ('微软雅黑', 32), fg = 'white', bg = '#235DA9', width = 12)
labelSubmit.place(x=67,y=490)
#鼠标进出及点击
labelSubmit.bind('<Enter>',labelSubmitEnter)
labelSubmit.bind('<Leave>',labelSubmitLeave)
labelSubmit.bind('<Button-1>',labelSubmitClick)

#窗口中放置提示标签备用
labelReminder = tk.Label(login, text = '用户名或密码错误', font = ('微软雅黑', 10), bg = '#D8F2D5', fg = 'gray')


#显示窗口
login.mainloop()
