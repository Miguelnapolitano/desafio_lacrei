from django.db import models
import uuid

from professional.models import Professional

class Visit(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    date = models.DateTimeField()
    professional = models.ForeignKey(Professional, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)