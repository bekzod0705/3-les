from django.db import models

# Create your models here.

class TeacherModel(models.Model):
    name=models.CharField(max_length=80,default='')
    age=models.PositiveIntegerField()
    ismarried=models.BooleanField(default=False)
    salary=models.PositiveIntegerField()
    def __str__(self) -> str:
        return self.name