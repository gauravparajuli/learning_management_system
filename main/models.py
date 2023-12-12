from django.db import models

# Create your models here.
class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    qualification = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=20)
    skills = models.TextField()

    def __str__(self) -> str:
        return self.full_name

class CourseCategory(models.Model):

    class Meta:
        verbose_name_plural = 'course categories'

    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title

class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    featured_img = models.ImageField(upload_to='course_images', null=True)
    techs = models.TextField(null=True)

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    qualificaton = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=20)
    address = models.TextField()
    intrested_categories = models.TextField()