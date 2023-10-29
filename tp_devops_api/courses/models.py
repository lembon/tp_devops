from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    birthdate = models.DateField(null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.last_name}, {self.first_name}"