from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from datetime import datetime

# Create your models here.


class Audit(models.Model):
    name = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="auditeur")
    readers = models.ForeignKey(User, on_delete=models.CASCADE, related_name="relecteur")

    create_by = models.DateTimeField(auto_now_add=True)
    update_by = models.DateTimeField(auto_created=True)


    # def save(self, *args, **kwargs):
    #     self.update_by = datetime.time
    #     super().save(*args, **kwargs)



    def get_detail_url(self):
        return reverse('audit:detail-audit', kwargs={'pk': self.pk})
    
    def get_update_url(self):
        return reverse('audit:update-audit', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('audit:delete-audit', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s ' % (self.name)


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
