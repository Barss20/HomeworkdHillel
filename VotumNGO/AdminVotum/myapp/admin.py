from django.contrib import admin
from .models import Text
from .models import TelegramAdmin

admin.site.register(TelegramAdmin)
admin.site.register(Text)
