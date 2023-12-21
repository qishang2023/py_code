"""
根据需要创建对象是很常见的需求，在一个函数中，我们可以保留一些默认配置，然后根据需要进行修改。
例如，我们有一个创建用户的函数create_user，参数如下
● username （用户名）必填
● password （密码）	必填
● is_admin （是否是管理员）可选，默认为False
● is_active （是否已激活）可选，默认为True
● is_verified （是否已验证）可选，默认为False

create_user("john", "password")
create_user("jane", "password123", is_admin=True)
create_user("alice", "pass123", is_active=False, is_verified=True)
"""


def creat_user(username, password, is_admin=False, is_active=True, is_verified=False):
    print(
        f"username:{username},password:{password},is_admin:{is_admin},is_active:{is_active},is_verified:{is_verified}")


creat_user("john", "password")
creat_user("jane", "password123", is_admin=True)
creat_user("alice", "pass123", is_active=False, is_verified=True)
