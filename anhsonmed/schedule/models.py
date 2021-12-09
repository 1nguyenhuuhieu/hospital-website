from django.db import models

# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField()
    MALE = 'male'
    FEMALE = 'female'
    SEX_CHOICES = [
        (MALE, 'Nam'),
        (FEMALE, 'Nữ')
    ]

    sex = models.CharField(
        max_length=6,
        choices=SEX_CHOICES
    )

    birth_date = models.DateField()

    DOCTOR = 'dr'
    NURSER = 'nu'
    STAFF = 'st'
    TECH = 'te'
    CLEANING = 'cl'
    STAFF_CHOICES = [
        (DOCTOR, 'Bác Sĩ'),
        (NURSER, 'Điều Dưỡng / Hộ Sinh'),
        (TECH, 'Kỹ Thuật Viên'),
        (STAFF, 'Nhân viên khối hành chính'),
        (CLEANING, 'Hộ Lý')
    ]

    staff_type = models.CharField(
        max_length=10,
        choices=STAFF_CHOICES
    )
    
   
    def __str__(self):
        return self.name

class Department(models.Model):
    title = models.CharField(max_length=200)
    staff = models.ManyToManyField(Staff)

    def __str__(self):
        return self.title

class Role(models.Model):
    title = models.CharField(max_length=200)
    department = models.ManyToManyField(Department)
    
    
    def __str__(self):
        return self.title

class Schedule(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    date = models.DateField()
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
