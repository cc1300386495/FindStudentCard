from django.db import models

# Create your models here.


class Lose(models.Model):
    student_id = models.IntegerField(primary_key=True)
    student_email = models.EmailField()
