from django.db import models

# Create your models here.
class Student(models.Model):
    age  = models.FloatField()
    systolicBP  = models.FloatField()
    diastolicBP  = models.FloatField()
    bs  = models.FloatField()
    bodytemp  = models.FloatField()
    heartrate  = models.FloatField()
    def __str__(self):
        return str(self.bodytemp)
    