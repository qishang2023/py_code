# **kwargs形参可以与 *args形参组合使用（*args必须在 **kwargs前面）

def func(name, *args, **kwargs):
    print(name)
    print(args, type(args))
    print(kwargs, type(kwargs))


func("王五")
func("赵六", "小红", "小明", "小刚")
func('张三', 1, 2, 3, 4, 5, 6, uname = '李四', age = 18)
