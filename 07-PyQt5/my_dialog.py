from PyQt5.QtWidgets import *
from ui.Ui_dialog import Ui_Dialog


class MyDialog(QDialog):
    """因为ui是对话框，所以继承于QDialog"""
    def __init__(self, parent=None):
        super().__init__(parent)
        # 实例化ui模块对象，调用setupUi()方法
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # 初始化UI界面
        self.init_ui()

    def init_ui(self):
        # 按钮信号的槽函数绑定
        self.ui.btnOk.clicked.connect(lambda : print('对话框点了ok'))
        self.ui.btnCancel.clicked.connect(lambda : print('对话框点了cancel'))
