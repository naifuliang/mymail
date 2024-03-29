# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Account_setting.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from utils.handlers.account import account_setting


class Ui_Login_window(object):
    def setupUi(self, Login_window):
        Login_window.setObjectName("Login_window")
        Login_window.resize(514, 521)
        Login_window.setMinimumSize(QtCore.QSize(514, 496))
        Login_window.setMaximumSize(QtCore.QSize(16000, 16000))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Login_window.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        Login_window.setFont(font)
        Login_window.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        Login_window.setToolTip("")
        Login_window.setAccessibleName("")
        self.Login_window = Login_window
        self.horizontalLayoutWidget = QtWidgets.QWidget(Login_window)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 40, 331, 131))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_MyMail = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(30)
        self.label_MyMail.setFont(font)
        self.label_MyMail.setObjectName("label_MyMail")
        self.horizontalLayout.addWidget(self.label_MyMail)
        self.Confirm = QtWidgets.QPushButton(Login_window)
        self.Confirm.setGeometry(QtCore.QRect(240, 440, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.Confirm.setFont(font)
        self.Confirm.setObjectName("Confirm")
        self.Password = QtWidgets.QLineEdit(Login_window)
        self.Password.setGeometry(QtCore.QRect(180, 370, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.Password.setFont(font)
        self.Password.setText("")
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setObjectName("Password")
        self.labelUsername = QtWidgets.QLabel(Login_window)
        self.labelUsername.setGeometry(QtCore.QRect(80, 320, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labelUsername.setFont(font)
        self.labelUsername.setObjectName("labelUsername")
        self.Username = QtWidgets.QLineEdit(Login_window)
        self.Username.setGeometry(QtCore.QRect(180, 320, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.Username.setFont(font)
        self.Username.setText("")
        self.Username.setObjectName("Username")
        self.labelPassword = QtWidgets.QLabel(Login_window)
        self.labelPassword.setGeometry(QtCore.QRect(80, 370, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labelPassword.setFont(font)
        self.labelPassword.setObjectName("labelPassword")
        self.labelUsername_2 = QtWidgets.QLabel(Login_window)
        self.labelUsername_2.setGeometry(QtCore.QRect(80, 190, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labelUsername_2.setFont(font)
        self.labelUsername_2.setObjectName("labelUsername_2")
        self.SMTP_Server = QtWidgets.QLineEdit(Login_window)
        self.SMTP_Server.setGeometry(QtCore.QRect(190, 190, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.SMTP_Server.setFont(font)
        self.SMTP_Server.setText("")
        self.SMTP_Server.setObjectName("SMTP_Server")
        self.labelUsername_3 = QtWidgets.QLabel(Login_window)
        self.labelUsername_3.setGeometry(QtCore.QRect(350, 190, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labelUsername_3.setFont(font)
        self.labelUsername_3.setObjectName("labelUsername_3")
        self.SMTP_Port = QtWidgets.QLineEdit(Login_window)
        self.SMTP_Port.setGeometry(QtCore.QRect(390, 190, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.SMTP_Port.setFont(font)
        self.SMTP_Port.setText("")
        self.SMTP_Port.setObjectName("SMTP_Port")
        self.POP3_Server = QtWidgets.QLineEdit(Login_window)
        self.POP3_Server.setGeometry(QtCore.QRect(190, 230, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.POP3_Server.setFont(font)
        self.POP3_Server.setText("")
        self.POP3_Server.setObjectName("POP3_Server")
        self.labelUsername_4 = QtWidgets.QLabel(Login_window)
        self.labelUsername_4.setGeometry(QtCore.QRect(350, 230, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labelUsername_4.setFont(font)
        self.labelUsername_4.setObjectName("labelUsername_4")
        self.POP3_Port = QtWidgets.QLineEdit(Login_window)
        self.POP3_Port.setGeometry(QtCore.QRect(390, 230, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.POP3_Port.setFont(font)
        self.POP3_Port.setText("")
        self.POP3_Port.setObjectName("POP3_Port")
        self.labelUsername_5 = QtWidgets.QLabel(Login_window)
        self.labelUsername_5.setGeometry(QtCore.QRect(80, 230, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labelUsername_5.setFont(font)
        self.labelUsername_5.setObjectName("labelUsername_5")
        self.labelUsername_6 = QtWidgets.QLabel(Login_window)
        self.labelUsername_6.setGeometry(QtCore.QRect(80, 270, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labelUsername_6.setFont(font)
        self.labelUsername_6.setObjectName("labelUsername_6")
        self.Security_Option = QtWidgets.QComboBox(Login_window)
        self.Security_Option.setGeometry(QtCore.QRect(180, 271, 241, 31))
        self.Security_Option.setObjectName("Security_Option")
        self.Security_Option.addItem("")
        self.Security_Option.addItem("")
        self.Security_Option.addItem("")

        self.retranslateUi(Login_window)
        QtCore.QMetaObject.connectSlotsByName(Login_window)
        Login_window.setTabOrder(self.Username, self.Password)
        Login_window.setTabOrder(self.Password, self.Confirm)
        self.Confirm.clicked.connect(self.account_setting)

    def retranslateUi(self, Login_window):
        _translate = QtCore.QCoreApplication.translate
        Login_window.setWindowTitle(_translate("Login_window", "Account Settings"))
        self.label_MyMail.setText(_translate("Login_window", "My Mail"))
        self.Confirm.setText(_translate("Login_window", "Confirm"))
        self.labelUsername.setText(_translate("Login_window", "Username:"))
        self.labelPassword.setText(_translate("Login_window", "Password:"))
        self.labelUsername_2.setText(_translate("Login_window", "SMTP Server"))
        self.labelUsername_3.setText(_translate("Login_window", "Port"))
        self.labelUsername_4.setText(_translate("Login_window", "Port"))
        self.labelUsername_5.setText(_translate("Login_window", "POP3 Server"))
        self.labelUsername_6.setText(_translate("Login_window", "Security"))
        self.Security_Option.setItemText(0, _translate("Login_window", "SSL (Recommended)"))
        self.Security_Option.setItemText(1, _translate("Login_window", "Plain"))
        self.Security_Option.setItemText(2, _translate("Login_window", "TLS"))
    def account_setting(self):
        account_setting(self.SMTP_Server.text(), self.SMTP_Port.text(), self.POP3_Server.text(), self.POP3_Port.text(), self.Username.text(), self.Password.text(), self.Security_Option.currentIndex())
        self.Login_window.close()