from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=36)
    last_name = models.CharField(max_length=36)
    email = models.CharField(max_length=100, unique=True)
    password_hash = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=36)
    role = models.TextChoices('role', 'guest host admin')
    created_at = models.DateField()
    

class Message(models.Model):
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE)
    message_body = models.TextField()
    sent_at = models.DateField()


class Conversation(models.Model):
    participants_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField()


