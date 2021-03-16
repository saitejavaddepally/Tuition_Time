
from django import forms
from account.models import user_register

class ModelsService:
    def __init__(self):
        pass

    def user_new_save(self, user):
        user.save()

    def user_new_update(self, user):
        user.save()
    
    def user_new_delete(self, user , id): 
        user.delete()

    def user_new_get(self, user,  id):
        user.get(id = id)
    
    def users_all(self, users):
        users.all()

        