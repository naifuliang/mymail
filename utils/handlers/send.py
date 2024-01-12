from socket import socket

from utils.protocols.smtp import send_email_smtp
from utils.DB_Operations.models import Accounts

def send_mail(to, subject, content):
    account = Accounts.select().where(Accounts.id == 1).first()
    result = send_email_smtp(
        sender=account.username,
        recipient=to,
        subject=subject,
        body=content,
        server=account.SMTP_server,
        port=account.SMTP_port,
        username=account.username,
        password=account.password,
        security=account.Security,
        client_hostname='localhost'
    )
    return result