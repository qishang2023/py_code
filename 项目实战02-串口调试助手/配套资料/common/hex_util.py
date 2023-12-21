import binascii
import re

HEX_PATTERN = r'^([0-9a-fA-F]{2})*([0-9a-fA-F]{2})?$'

def remove_all_0x(hex_string):
    if not hex_string.startswith("0x"):
        return hex_string

    str_len = len(hex_string)
    # 将字符串拆分成两个字符一组的列表
    hex_list = [hex_string[i + 2:i + 4] for i in range(0, str_len, 4)]
    return "".join(hex_list)


def is_hex_string(hex_string: str) -> bool:
    """
    检查是否是16进制字符串格式
    :param hex_string:
    :return:
    """
    # 去除字符串中的空格
    hex_string = hex_string.replace(" ", "")
    hex_string = remove_all_0x(hex_string)
    match = re.match(HEX_PATTERN, hex_string)
    return bool(match)


def hex_string_to_bytes(hex_string: str) -> bytes:
    """
    将如下格式的字符串转成bytes字节数组（有无空格皆可）
    12 F2 34 72 E2
    0x12 0xF2 0x34 0x72 0xE2
    :param hex_string: 16进制内容的字符串
    :return: 字节数组
    """
    # 去除字符串中的空格
    hex_string = hex_string.replace(" ", "")

    # 检查字符串是否包含"0x"，如果是，则去除每个字节开头的"0x"
    joined_str = remove_all_0x(hex_string)
    byte_array = bytearray.fromhex(joined_str)

    return byte_array


def bytes_to_hex_string(byte_array: bytes) -> str:
    """
    将字节数组转成16进制字符串，用空格分割。
    :param byte_array: 字节数组
    :return: 16进制字符串,以空格分割  格式如下：12 F2 34 72 E2
    """
    # 将字节数组中的每个字节转换为对应的十六进制字符串，并去除开头的"0x"
    hex_list = [hex(byte)[2:].zfill(2) for byte in byte_array]

    # 将十六进制字符串列表中的每个字符串添加空格，并连接成一个字符串
    return " ".join(hex_list).upper()


def string_to_hex_string(string: str, encoding="UTF-8") -> str:
    """
    将字符串转成16进制字符串，用空格分割。
    :param string:  字符串
    :param encoding: 字符串的转成字节数组的编码集
    :return:  16进制字符串,以空格分割, 格式如下：12 F2 34 72 E2
    """
    decode_str = binascii.hexlify(string.encode(encoding)).decode(encoding)
    # 每个两个加一个空格
    length = len(decode_str)
    decode_str_arr = [decode_str[i: i + 2] for i in range(0, length, 2)]
    return " ".join(decode_str_arr)


def hex_string_to_string(hex_string: str, encoding="UTF-8") -> str:
    """
    将16进制字符串转成字符串，如果包含0x，则自动去除0x
    :param hex_string:  16进制字符串
    :param encoding: 字符串的转成字节数组的编码集
    :return:  字符串
    """
    hex_string = hex_string.replace(" ", "")
    # 如果包含0x，则自动去除每个字节的0x
    hex_string = remove_all_0x(hex_string)

    return binascii.unhexlify(hex_string).decode(encoding)


if __name__ == '__main__':
    print("------------------------------16进制字符串=>字节数组------------------------------")
    print(hex_string_to_bytes("0x12 0xF2 0x34 0x72 0xE2"))
    print(hex_string_to_bytes("12 F2 34 72 E2"))

    print("------------------------------字节数组=>16进制字符串------------------------------")

    print(bytes_to_hex_string(bytes([0x12, 0xF2, 0x34, 0x72, 0xE2])))
    print(bytes_to_hex_string(b'\x12\xf24r\xe2'))
    print(bytes_to_hex_string(bytearray(b'\x12\xf24r\xe2')))

    print("-----------------------------字符串=>16进制字符串------------------------------")
    print(string_to_hex_string("XYZ123^_^", "gbk"))
    print("-----------------------------16进制字符串=>字符串------------------------------")
    print(hex_string_to_string("58 59 5a 31 32 33 5e 5f 5e", "gbk"))
    print(hex_string_to_string("58595a3132335e5f5e", "gbk"))

    print("-----------------------------检查是否是16进制字符串------------------------------")
    print(is_hex_string("58595a3132335e5f5e"))
    print(is_hex_string("58 59 5a 31"))
    print(is_hex_string("0x58 0x59 0x5a 0x31"))
    print(is_hex_string("av12"))
    print(is_hex_string("av1"))
    print(is_hex_string("噶"))
    print(is_hex_string(""))
