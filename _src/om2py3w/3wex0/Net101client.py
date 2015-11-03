# _*_ coding:utf-8 _*_
import socket
import sys
from sys import argv

script, writeread = argv

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)

# 发送 read给服务器， 请求返回日记
# 脚本附加 write 参数 , 代表写日记， 否则，发送read 
# 输入日记，发送给服务器端

print "输入一行日记，输入exit，否则退出日记"
				
line = raw_input('> ')

while line <> 'exit':   # 输入不是exit，则执行写日记功能
	if line <> 'read':   # 把日记内容发给服务器
		sent = sock.sendto(line, server_address)
		print "日记已保存"
		line = raw_input('> ')
 
	else: # 发送 read ，接收并显示日记内容 
		sock.sendto('read', server_address)
		print "显示网络日记."
		data, server = sock.recvfrom(4096)
	
		print "-" * 40
		print data
		line = raw_input('> ')

print >>sys.stderr, 'closing socket'
sock.close()