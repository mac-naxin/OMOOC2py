
# _*_ coding:utf-8 _*_

from  Tkinter import *
import sys
reload(sys)
sys.setdefaultencoding('utf8')

root = Tk()
# root.geometry('600x30+400+400')

class Application(Frame):  

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()


	def writeInput(self, event):  # 定义写函数
		
		line = self.line.get()
		target = open('dairy.txt', 'a+')
		target.write('%s\n'  % line)
		target.close()
		self.insertText(line)
#		self.text.see(END)
		self.myEntry.delete(0, END)

	def insertText(self, line):
		self.text.config(state=NORMAL)
		self.text.insert(END, line + "\n")
		self.text.see(END)
		self.text.config(state=DISABLED)

    	
	def createWidgets(self): # 定义三种控件

# 定义 输入框myEntry
		self.line = StringVar(self)
		self.myEntry = Entry(self, textvariable=self.line, width = 80)
		self.myEntry.bind("<Return>", self.writeInput)  # 回车即执行写入函数
		self.myEntry.grid(row = 0, column = 1, sticky = W)
		self.myEntry.focus_set()

# 定义输出框showbox
		self.text = Text(self)
		self.text.grid(columnspan = 2, sticky = W)

		rd = open('dairy.txt', 'r')
		lines = rd.read()
		self.text.insert(END, lines)
		self.text.config(state=DISABLED)		
		self.text.see(END)


# 定义退出按钮
		self.myQuit =Button(self, text="QUIT", fg="red", command=self.quit)
		self.myQuit.grid(row = 2, column = 0, sticky = W)

		

def main():
	app = Application(master = root)
	app.master.title('简单笔记本')
	app.mainloop()

if __name__ == "__main__":
	main()







		