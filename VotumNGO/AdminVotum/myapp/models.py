from django.db import models

class Text(models.Model):
    title = models.CharField(max_length=10, default='Название')
    content = models.TextField(max_length=4096)

    def __str__(self):
        return self.title


class TelegramAdmin(models.Model):
    title = models.CharField(max_length=20, default='Nickname')
    user_id = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
