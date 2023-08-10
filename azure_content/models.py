from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=500, unique=True)
    description = models.CharField(max_length=500,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 