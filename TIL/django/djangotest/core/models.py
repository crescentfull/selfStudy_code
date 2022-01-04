from django.db import models

# Create your models here.
class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True, null = True)

    class Meta:
        abstract = True #다른 앱 사용 가능하도록 