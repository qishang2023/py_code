"""
# 1. 导入模块socket

# 参数1：地址类型：AddressFamily：AF_INET(IPv4) AF_INET6(IPv6)
# 参数2：协议类型：SOCK_STREAM(TCP) SOCK_DGRAM(UDP)
# 2. 创建socket套接字：套接字对象 = socket.socket(family=地址类型, type=协议类型)

# 3. 设置允许发送广播：套接字.setsockopt(当前设置的影响范围, 要配置的属性名, 要配置的属性值(允许广播))
# 4. 发送数据(注意是广播地址)：套接字.sendto(要发送的数据的字节码, (广播地址, 目的端口))
# 5. 关闭套接字：套接字.close()
"""

