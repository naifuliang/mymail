import base64
import socket
import ssl
import re
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
from datetime import datetime

def parse_email(email_content):
    # 使用Parser从字符串中解析邮件
    msg = Parser().parsestr(email_content)

    # 解析发件人
    from_email = msg.get('From')

    # 解析主题
    subject = msg.get('Subject')

    # 解析正文
    body = ""
    if msg.is_multipart():
        # 对于多部分邮件，找到文本部分
        for part in msg.walk():
            ctype = part.get_content_type()
            cdispo = str(part.get('Content-Disposition'))

            # 跳过附件和HTML
            if 'attachment' in cdispo or ctype == 'text/html':
                continue
            payload = part.get_payload(decode=True)
            if payload is not None:
                body = payload.decode('utf-8', errors='replace')
                break
    else:
        # 对于非多部分邮件，直接获取正文
        payload = msg.get_payload(decode=True)
        if payload is not None:
            body = payload.decode('utf-8', errors='replace')

    return from_email, subject, body


def check_login(server, port, username, password, security=None):
    def send_command(sock, cmd):
        sock.send(cmd)
        response = b""
        while True:
            data = sock.recv(1024)
            response += data
            if len(data) < 1024:
                break
        return response

    # 根据安全设置创建套接字
    if security == 'SSL':
        context = ssl.create_default_context()
        sock = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=server)
    else:
        sock = socket.socket(socket.AF_INET)

    # 连接到服务器
    sock.connect((server, port))
    print(sock.recv(1024).decode())

    # 如果使用STARTTLS，启动TLS
    if security == 'STARTTLS':
        context = ssl.create_default_context()
        recv = send_command(sock, b'STLS\r\n')
        if not recv.startswith(b'+OK'):
            return "STARTTLS failed"

        sock = context.wrap_socket(sock, server_hostname=server)
        print(sock.recv(1024).decode())

    # 登录
    recv = send_command(sock, b'USER ' + username.encode() + b'\r\n')
    if not recv.startswith(b'+OK'):
        return "Username not accepted"

    recv = send_command(sock, b'PASS ' + password.encode() + b'\r\n')
    if not recv.startswith(b'+OK'):
        return "Password not accepted"
    return "Login Success"


def receive_email(server, port, username, password, security=None):
    def send_command(sock, cmd):
        sock.send(cmd)
        response = sock.recv(1024)
        return response
    def send_command_content(sock, cmd):
        sock.send(cmd)
        response = b""
        while True:
            data = sock.recv(2048)
            response += data
            if data.endswith(b'\r\n.\r\n'):  # 检查邮件结束标记
                break
        return response

    if security == 'SSL':
        context = ssl.create_default_context()
        sock = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=server)
    else:
        sock = socket.socket(socket.AF_INET)

    sock.connect((server, port))
    print(sock.recv(2048).decode())

    if security == 'STARTTLS':
        context = ssl.create_default_context()
        recv = send_command(sock, b'STLS\r\n')
        if not recv.startswith(b'+OK'):
            return "STARTTLS failed"
        sock = context.wrap_socket(sock, server_hostname=server)
        print(sock.recv(2048).decode())

    send_command(sock, b'USER ' + username.encode() + b'\r\n')
    send_command(sock, b'PASS ' + password.encode() + b'\r\n')

    resp = send_command(sock, b'LIST\r\n')
    if not resp.startswith(b'+OK'):
        return "LIST command failed"

    # 解析邮件数量
    messages = int(resp.split(b'\n')[0].split()[1])
    emails = []
    for i in range(1, messages + 1):
        print(f"\nFetching email {i}/{messages}")

        # 获取邮件
        resp = send_command_content(sock, f'RETR {i}\r\n'.encode())
        mail = resp.decode()
        mail = mail.replace('.', '')
        mail = '\n'.join(mail.split('\n')[1:])  # 去掉第一行 '+OK message follows'
        email_from, email_subject, email_body = parse_email(mail)
        emails.append({
            'from': email_from,
            'subject': email_subject,
            'body': email_body
        })
        delete_resp = send_command(sock, f'DELE {i}\r\n'.encode())
        print(f"Deleting email {i}: {delete_resp.decode()}")
    send_command(sock, b'QUIT\r\n')
    sock.close()
    return emails

if __name__ == '__main__':
    # Example usage
    print('SSL')
    result = receive_email(
        server='pop.titan.email',
        port=995,  # 995 for SSL, 110 for STARTTLS
        username='test@ilnf.space',
        password='cqnr)J@124',
        security='SSL'
    )
    print(result)


