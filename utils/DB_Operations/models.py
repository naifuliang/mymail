from peewee import Model, MySQLDatabase
import peewee

db = MySQLDatabase(database='mymail', host="localhost", user='mymail', passwd='mymail', port=3306)

class Accounts(Model):
    id = peewee.AutoField(primary_key=True)
    SMTP_server = peewee.TextField()
    SMTP_port = peewee.IntegerField()
    POP3_server = peewee.TextField()
    POP3_port = peewee.IntegerField()
    username = peewee.TextField()
    password = peewee.TextField()
    Security = peewee.TextField()
    class Meta:
        database = db

class In_box(Model):
    id = peewee.AutoField(primary_key=True)
    sender = peewee.TextField()
    subject = peewee.TextField()
    content = peewee.TextField()
    class Meta:
        database = db