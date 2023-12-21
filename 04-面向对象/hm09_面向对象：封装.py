"""
需求：
• 进入某 Web 项目登录页面， 输入用户名、 密码、 验证码之后登录系统
要求：
• 用户名为'admin'，密码为'123abc'，验证码为：'abcd'，返回登陆成功，否则，返回登陆失败

类名：LoginPage
实例属性：用户名username、密码password、验证码verify_code
实例方法：
    __init__(): 添加属性
    __str__(): 返回字符串格式的属性信息
    login(): 登陆
"""


class LoginPage:
    def __init__(self, username, password, verify_code):
        self.username = username
        self.password = password
        self.verify_code = verify_code

    def __str__(self):
        return f'用户名：{self.username},密码：{self.password},验证码：{self.verify_code}'

    def login(self):
        if self.username == 'admin' and self.password == '123abc' and self.verify_code == 'abcd':
            return '登陆成功'
        else:
            return '登陆失败'


name = input('请输入用户名：')
password = input('请输入密码：')
verify_code = input('请输入验证码：')
login = LoginPage(name, password, verify_code)
print(login)
print(login.login())
