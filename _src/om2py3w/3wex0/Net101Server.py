# _*_ coding:utf-8 _*_
import socket
import sys
# 创建socket
# 绑定端口和IP host
# 对用户的请求进行判断，如收到 data 是 read  则返回 日志记录（文件）
# 如果收到其他数据，则接收data  写入文件

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

def write(data):
	target = open('dairy.txt', 'a')
	target.write(data + '\n')
	target.close()

	
	
		

while  True:
	
	data, address = sock.recvfrom(4096)

	if data == "read":  # 返回日记文件， 无效的why
		print >>sys.stderr, '\nwaiting to read dairy'
		target = open('dairy.txt')
		record = target.read()
		sock.sendto(record, address)
		target.close()

#		print >>sys.stderr, 'sent %s bytes back to %s' % (sent, address)
	else:            # 把data写入日记
		write(data)   # 把data 传入write函数中执行

