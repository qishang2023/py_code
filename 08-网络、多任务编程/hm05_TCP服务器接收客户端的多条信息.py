"""
# 0. 导入socket

# 参数1：地址类型：AddressFamily：AF_INET(IPv4) AF_INET6(IPv6)
# 参数2：协议类型：SOCK_STREAM(TCP) SOCK_DGRAM(UDP)
# 1. 创建socket套接字：套接字对象 = socket.socket(family=地址类型, type=协议类型)

# 如果服务ip是空字符串，代表所有网卡的端口都监听数据
# 2. bind绑定ip和port ： 套接字.bind((服务器IP, 服务器端口))

# 3. listen使套接字设置为被动模式： 套接字.listen(指定最大连接数)
# 4. accept等待客户端的链接：客户端套接字, 客户端地址 = 套接字.accept()
# 5. recv/send接收发送数据： 套接字.recv(指定接收最大长度), 套接字.send(要发送的数据的字节码)
# 6. tcp关闭套接字： 套接字.close()
"""

