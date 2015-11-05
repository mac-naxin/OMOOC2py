# _*_ coding:utf-8 _*_
import socket
import sys
from sys import argv

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print "请输入服务器地址："
sdb = raw_input('> ')
# server_address = ('localhost', 10000)
server_address = (sdb, 10000)

print "请输入一行日记，如输入exit，退出日记，如输入read, 则打印日记"
				
line = raw_input('> ')

while line <> 'exit':   # 输入不是exit，则执行写日记功能
	if line <> 'read':   # 把日记内容发给服务器
		sent = sock.sendto(line, server_address)
		data, server = sock.recvfrom(4096)
		print data
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