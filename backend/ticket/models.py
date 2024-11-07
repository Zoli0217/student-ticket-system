from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    status_choices = [
        ('new','new'),
        ('pending', 'pending'),
        ('done', 'done'),
    ]

    status = models.CharField(max_length=7, choices=status_choices)

    def __str__(self):
        return f"{self.user} - {self.subject} #{self.id}"