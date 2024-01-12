from utils.DB_Operations.models import In_box

def delete_email(id):
    In_box.delete().where(In_box.id == id).execute()