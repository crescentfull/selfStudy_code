from django.db import models

from core.models import TimeStamp
from user.models import User
# Create your models here.
class Post(TimeStamp):
    title   = models.CharField(max_length=200)
    content = models.TextField()
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'posts'