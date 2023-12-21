import ipaddress
import os
import socket
import time

BUFSIZE = 2048


class Color:
    """
    颜色枚举类
    """
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    PURPLE = 35
    CYAN = 36


def wrap_color(msg, color):
    """
    包装颜色
    :param msg: 要包装的字符串
    :param color: 颜色
    :return:
    """
    return f"\033[{color}m{msg}\033[0m"


def get_hosts(r1, r2):
    """
    功能：获取本地所有IP地址，过滤出r1或r2开头的IP地址
    :param r1: IP地址前缀1
    :param r2: IP地址前缀2
    :return: 本地所有IP地址列表
    """
    # 获取所有本机ip
    hosts = socket.gethostbyname_ex(socket.gethostname())[2]
    # 过滤出192或172开头的IP地址
    hosts_filter = [host for host in hosts if host.startswith(r1) or host.startswith(r2)]

    return hosts_filter


def get_local_ip():
    """
    获取本机所有IP
    :return: IP列表
    """
    local_ips = {"127.0.0.1"}
    for ip in socket.gethostbyname_ex(socket.gethostname())[2]:
        local_ips.add(ip)

    local_ips = list(local_ips)
    local_ips.sort(reverse=True)
    return local_ips


def calculate_broadcast_address(host, mask_bits):
    """
    功能：计算广播地址
    :param host: 主机IP地址
    :param mask_bits: 掩码的位数
    :return: 广播地址
    """
    # 将主机IP地址和掩码位数转换为网络对象
    network = ipaddress.ip_network(f"{host}/{mask_bits}", strict=False)

    # 获取广播地址
    broadcast_address = network.broadcast_address

    # 返回广播地址的字符串表示形式
    return str(broadcast_address)


def current_time_str():
    """获取当前时间"""
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def decode_data(recv_data: bytes):
    """将接收到的数据解码为字符串"""
    try:
        recv_msg = recv_data.decode("utf-8")
    except:
        recv_msg = recv_data.decode("gbk")
    return recv_msg


def clear_console():
    # 使用ANSI转义序列清空控制台内容
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    # 获取本地所有IP地址，过滤出192或172开头的IP地址
    hosts_filter = get_hosts("192", "172")
    print(hosts_filter)
    # 获取广播地址
    print(calculate_broadcast_address("192.16.1.102", 24))
    # 颜色测试
    print(wrap_color("测试", Color.RED))
    # 获取本地所有ip
    print(get_local_ip())
