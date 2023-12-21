"""
# 1. 导入socket模块

# 参数1：地址类型：AddressFamily：AF_INET(IPv4) AF_INET6(IPv6)
# 参数2：协议类型：SOCK_STREAM(TCP) SOCK_DGRAM(UDP)
# 2. 创建socket套接字：套接字对象 = socket.socket(family=地址类型, type=协议类型)

# 3. 建立tcp连接（和服务端建立连接）： 套接字.connect((服务器IP, 服务器端口))
# 4. 开始发送数据（到服务端）：  套接字.send(要发送的数据的字节码)
# 5. 接收对方回复的数据： 接收到字节码 = 套接字.recv(指定接收最大长度)
# 6. 关闭套接字 ： 套接字.close()
"""

