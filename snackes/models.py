
from django.db import models

class Snack(models.Model):
    name = models.CharField(max_length=64)
    purchaser=models.ForeignKey("auth.User", on_delete=models.CASCADE, default=1)
    description=models.TextField()
 

    def __str__(self):
        return self.name

