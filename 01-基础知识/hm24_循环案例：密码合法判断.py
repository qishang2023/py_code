"""
需求：判断登录密码hhew2383dW_fkf&E@^是否合法。
1. 密码必须是数字、字母(大小写都可以)、和下划线，否则不合法
# 定义容器:保存所有的数字 字母 _
container = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
2. 如果密码合法,就输出"密码合法"
分析：
1. 定义容器，保存所有的数字 字母 _
2. for循环遍历密码中每一个元素
3. 判断每一个元素是否合法
4. 如果不合法，执行break
"""
container = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
for i in 'hhew2383dW_fkf&E@^':
    if i not in container:
        print(f"密码不合法，不能包含{i}")
        # print('密码不合法')
        break
else:
    print('密码合法')
