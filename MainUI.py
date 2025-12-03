from PyQt5 import QtWidgets, QtCore
import sys
import testUI

# 1.创建PyQt窗口程序
app = QtWidgets.QApplication(sys.argv)
# 2.创建MainWindow窗口对象
mainWindow = QtWidgets.QMainWindow()

# 3.创建testUI窗口对象
ui = testUI.Ui_MainWindow()

# 4.初始化testUI窗口对象
ui.setupUi(mainWindow)

# 5.显示窗口
mainWindow.show()
# 定住窗口，点窗口右上角的关闭按键才退出
exit(app.exec_())
