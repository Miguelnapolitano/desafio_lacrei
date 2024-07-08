from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models
import uuid

class Professional(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    email = models.EmailField(unique=True)
    social_name = models.CharField(max_length=255, null=True, default=None)
    profession = models.CharField(max_length=255)
    
    groups = models.ManyToManyField(
        Group,
        related_name="professional_groups",  # Nome personalizado
        blank=True,
        help_text="The groups this user belongs to. A user may belong to multiple groups."
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="professional_permissions",  # Nome personalizado
        blank=True,
        help_text="Specific permissions for this user."
    )

class Address(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)    
    user = models.ForeignKey("professional.Professional",
                                on_delete=models.CASCADE)
    street = models.CharField(max_length=100)
    number = models.IntegerField()
    complement = models.CharField(max_length=50,null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=50)
    neighborhood = models.CharField(max_length=50)