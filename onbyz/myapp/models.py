from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    passing_out_date = models.DateField()
    student_image = models.ImageField(upload_to='student_images/', blank=True, null=True)

    def __str__(self):
        return self.name

