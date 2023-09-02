from django.db import models
from django.contrib.auth.models import UserManager


class UserManager(UserManager):
    def create_user(self, username, password=None):
        if username == None:
            raise ValueError('Username should not be empty')

        user = self.model(
            username=username
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username=username, password=password)
        user.is_admin = True
        user.save()
        return user
