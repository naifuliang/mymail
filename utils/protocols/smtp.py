import socket
import ssl
import base64

def send_email_smtp(sender, recipient, subject, body, server, port, username=None, password=None, security=None, client_hostname='localhost'):
    message = f"From: {sender}\r\nTo: {recipient}\r\nSubject: {subject}\r\n\r\n{body}"
    # 函数用于发送命令并接收响应
    def send_command(sock, cmd):
        sock.send(cmd)
        response = sock.recv(1024)
        return response
    # 根据安全设置创建套接字
    if security == 'SSL':
        context = ssl.create_default_context()
        sock = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=server)
    else:
        sock = socket.socket(socket.AF_INET)
    # 连接到服务器
    print(server, port)
    sock.connect((server, port))
    recv = send_command(sock, f'EHLO {client_hostname}\r\n'.encode())
    recv = sock.recv(1024)
    # 如果使用STARTTLS，启动TLS
    if security == 'STARTTLS':
        context = ssl.create_default_context()
        recv = send_command(sock, b'STARTTLS\r\n')
        if not recv.startswith(b'220'):
            return "STARTTLS failed"

        sock = context.wrap_socket(sock, server_hostname=server)
        recv = send_command(sock, f'EHLO {client_hostname}\r\n'.encode())

    # 进行身份验证
    if username and password:
        recv = send_command(sock, b'AUTH LOGIN\r\n')
        if not recv.startswith(b'334'):
            print(recv.decode())
            return "Authentication command failed"

        recv = send_command(sock, base64.b64encode(username.encode()) + b'\r\n')
        if not recv.startswith(b'334'):
            return "Username not accepted"

        recv = send_command(sock, base64.b64encode(password.encode()) + b'\r\n')
        if not recv.startswith(b'235'):
            return "Password not accepted"

    recv = send_command(sock, f'MAIL FROM:<{sender}>\r\n'.encode())
    if not recv.startswith(b'250'):
        return "MAIL FROM command failed"

    recv = send_command(sock, f'RCPT TO:<{recipient}>\r\n'.encode())
    if not recv.startswith(b'250'):
        return "RCPT TO command failed"

    recv = send_command(sock, b'DATA\r\n')
    if not recv.startswith(b'354'):
        return "DATA command failed"

    recv = send_command(sock, (message + "\r\n.\r\n").encode())
    if not recv.startswith(b'250'):
        return "Message body not accepted"

    send_command(sock, b'QUIT\r\n')

    sock.close()
    return "Email sent successfully"
if __name__ == '__main__':
    # Example usage
    print('tls')
    result = send_email_smtp(
        sender='test@ilnf.space',
        recipient='naifu.liang@foxmail.com',
        subject='Test Subject11',
        body='This is the body of the email. TLS is used.',
        server='smtp.titan.email',
        port=587,  # 465 for SSL, 587 for STARTTLS
        username='test@ilnf.space',
        password='cqnr)J@124',
        security='STARTTLS',
        client_hostname='naifu'
    )
    print(result)
    print('ssl')
    result = send_email_smtp(
        sender='test@ilnf.space',
        recipient='naifu.liang@foxmail.com',
        subject='Test Subject22',
        body='This is the body of the email. SSL is used.',
        server='smtp.titan.email',
        port=465,  # 465 for SSL, 587 for STARTTLS
        username='test@ilnf.space',
        password='cqnr)J@124',
        security='SSL',
        client_hostname='naifu'
    )
    print(result)

