import uuid
from django.db import models
from datetime import datetime

# Create your models here.

class History(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    op = models.CharField(max_length=10)
    result = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.now)