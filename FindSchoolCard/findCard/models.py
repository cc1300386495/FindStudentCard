from django.db import models

# Create your models here.


class Find(models.Model):
    student_id = models.IntegerField(primary_key=True)
    location = models.CharField(max_length=200)
    find_day = models.DateTimeField()
