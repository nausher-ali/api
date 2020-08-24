from django.db import models

# Create your models here.
class Mem(models.Model):
    name = models.CharField(max_length = 256)
    phone = models.CharField(max_length = 15)
    address = models.TextField(blank=True, null=True)
    position = models.CharField(max_length = 128)
    dob = models.DateField()
    vertical = models.CharField(max_length = 128)
    department = models.CharField(max_length = 256)

    def __str__(self):
        return self.name
