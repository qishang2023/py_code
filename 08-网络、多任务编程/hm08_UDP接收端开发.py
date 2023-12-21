"""
# 1. 导入模块socket

# 参数1：地址类型：AddressFamily：AF_INET(IPv4) AF_INET6(IPv6)
# 参数2：协议类型：SOCK_STREAM(TCP) SOCK_DGRAM(UDP)
# 2. 创建socket套接字：套接字对象 = socket.socket(family=地址类型, type=协议类型)

# 3. 绑定IP&端口（必选）: 套接字.bind((服务器IP, 服务器端口))
# 4. 接收数据：接收的数据, 对方地址 = 套接字.recvfrom(指定接收最大长度)
# 5. 关闭套接字：套接字.close()
"""


