from tortoise.models import Model
from tortoise import fields


class user(Model):
    id = fields.IntField(primary_key=True)
    fullname = fields.TextField()

    username = fields.TextField()
    password = fields.TextField()

    def __str__(self):
        pass
