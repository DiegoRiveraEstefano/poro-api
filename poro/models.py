from django.db import models
from django.contrib.auth.models import User
import uuid


def get_random_hash():
    return hash(uuid.uuid4())


class Poro(models.Model):
    UUID = models.TextField(null=False, primary_key=True, editable=True)
    hash_key = models.TextField(auto_created=get_random_hash)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=32, default="poro")