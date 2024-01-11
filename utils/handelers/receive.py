from utils.protocols.pop3 import receive_email
from utils.DB_Operations.models import Accounts, In_box

def receive():
    account = Accounts.select().where(Accounts.id == 1).first()
    result = receive_email(
        server=account.POP3_server,
        port=account.POP3_port,
        username=account.username,
        password=account.password,
        security=account.Security
    )
    for email in result:
        In_box.create(sender=email['from'], subject=email['subject'], content=email['body'])

def get_all():
    # get all email from the database
    emails = In_box.select()
    result = []
    for email in emails:
        result.append({
            'id': email.id,
            'sender': email.sender,
            'subject': email.subject,
            'content': email.content
        })
    return result