# _*_ coding:utf-8 _*_
# from Tkinter import *  # 导入 Tkinter 模块 or 
# 按课程提示，更新Tcl/Tk 到 ActiveTcl 8.5.18 
# 首先需要有一个文本框， 输入后，get给变量 text.get()
# 从一个最小框架出发
# 至少需要两个文本框Entry组件，一个用于输入，一个用于显示
# 如何能省略保存按钮

import Tkinter as tk
# from  Tkinter import *
import sys


class MainApp:

	def __init__(self, master):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

# 定义函数，文本框绑定回车时间，按下回车，将控件的内容写入,同时显示在显示框内，并删除输入框
	def handleInput(self, event):
		line = self.new_input
    	target = open('dairy.txt', 'a')
    	target.write('%s\n' % line)  # 换行，使一条记录是一行
    	target.close()

    	self.showbox.insert(END, "%s \n" % line)
    	self.showbox.see(END)
    	self.myEntry.delete(0, END)

	def myWidgets(self):  # 定义所有的控件
		self.new_input = StringVar(self)  # 输入字符变量

# 定义 输入框myEntry
		self.myEntry = Entry(self, textvariable = self.new_input, width = 80)
		self.myEntry.bind("<key-Return", self.handleInput)  # 回车即执行写入函数
		self.myEntry.grid(row = 0, column = 1, sticky = W)
		self.myEntry.focus_set()

# 定义输出框showbox
		self.showbox = ScrolledText(self)
		self.showbox.grid(columnspan = 2, sticky =W)
		target = open('dairy.txt', 'a')  # 有必要吗？
		self.showbox.insert(END, f, read())
		self.showbox.see(END)

# 定义退出按钮
		self.myQuit =Button(self, text="QUIT", fg="red", command=self.quit)
		self.myQuit.grid(row = 2, column = 0, sticky = W)


def main():
	root = TK()
	root.title()
	root.geometry()
	app = MainApp(root)
	app.mainloop()

if __name__ == "__main__":
	main()





		