from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Audit(models.Model):
    name = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="auditeur")
    readers = models.ForeignKey(User, on_delete=models.CASCADE, related_name="relecteur")

    create_by = models.DateTimeField(auto_now_add=True)
    update_by = models.DateTimeField()


class Exploit(models.Model):
    CRITICAL_LEVEL = (
        ("VL", "Très faible"),
        ("L", "Faible"),
        ("M", "Moyen"),
        ("H", "Fort"),
    )

    audit = models.ForeignKey(Audit, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField()
    level_critical = models.CharField(max_length=2, choices=CRITICAL_LEVEL)
