# dairy append  publish _src/0m2py0w/0wex1/ README.md
# _*_ coding:utf-8 _*_
# A:一次接受输入一行日记
# B:保存为本地文件
# C:再次运行系统时，能打印出过往的所有日记
#
# ----思考过程----
#
# 为中文编码增加一行命令注释line2
# A=应为一个独立mod或函数，接收文本追加输入
# B=该函数带保存或不保存的功能
# C=运行脚本时，执行屏幕打印
# 101py需要和本地系统进行交互，所以要获取外部命令
from sys import argv  # 读取外部命令，与 import sys 有何区别？

script, writeread = argv

# 定义写日记的函数
def write(target):
	line = raw_input('> ')
	while line <> 'exit':   # 输入不是exit，则执行写日记功能
		target.write(line)
		target.write('\n')  # 换行，使一条记录是一行
		line = raw_input('> ')

	print "日记已保存"

# 提示接下来要写日记，如果脚本输入的是write，就执行写模块
# 否则，如果脚本输入其他（<>write），就执行屏幕打印功能
if writeread == 'write':  
    print "输入一行日记，输入exit，则退出日记"
    target = open('dairy.txt', 'a')
    write(target)
    target.close()
	

else: # 执行打印日记的功能
	print "显示我的日记."
	target = open('dairy.txt', 'r')
	print "-" * 40
	print target.read()
	target.close()







