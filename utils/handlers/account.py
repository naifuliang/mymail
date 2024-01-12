import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from utils.DB_Operations.models import Accounts

def account_setting(SMTP_server, SMTP_port, POP3_server, POP3_port, username, password, security):
    SMTP_port = int(SMTP_port)
    POP3_port = int(POP3_port)
    if security == 0:
        security = "SSL"
    elif security == 1:
        security = "PLAIN"
    elif security == 2:
        security = "STARTTLS"

    if Accounts.select().where(Accounts.id==1).exists():
        q = Accounts.update({Accounts.SMTP_server: SMTP_server, Accounts.SMTP_port: SMTP_port, Accounts.POP3_server: POP3_server,Accounts.POP3_port: POP3_port, Accounts.username: username, Accounts.password: password, Accounts.Security: security}).where(Accounts.id==1)
        q.execute()
    else:
        Accounts.create(SMTP_server=SMTP_server, SMTP_port=SMTP_port, POP3_server=POP3_server, POP3_port=POP3_port, username=username, password=password, Security=security)