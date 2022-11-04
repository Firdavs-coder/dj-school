from django.db import models

# Create your models here.


class Classes(models.Model):
    class_number = models.CharField(max_length=10)
    class_expire = models.CharField(max_length=150)
    class_teacher_name = models.CharField(max_length=150)
    class_teacher_image = models.ImageField(upload_to='classes')
    class_number_image = models.ImageField(upload_to='classes')

    def __str__(self):
        return self.class_number + " - " + self.class_teacher_name


class Teachers(models.Model):
    teacher_name = models.CharField(max_length=150)
    teacher_job = models.CharField(max_length=150)
    teacher_image = models.ImageField(upload_to='teachers')

    def __str__(self):
        return self.teacher_name + " - " + self.teacher_job


class ClassNumbers(models.Model):
    class_number = models.CharField(max_length=10)

    def __str__(self):
        return str(self.class_number)


class Schedule(models.Model):
    weekdays_tuple = (
        ('Dushanba', 'Dushanba'),
        ('Seshanba', 'Seshanba'),
        ('Chorshanba', 'Chorshanba'),
        ('Payshanba', 'Payshanba'),
        ('Juma', 'Juma'),
        ('Shanba', 'Shanba'),
    )
    weekdays = models.CharField(max_length=250, choices=weekdays_tuple)
    schedule_lesson_expire = models.CharField(max_length=150)
    schedule_lesson_name = models.CharField(max_length=150)
    class_id = models.ForeignKey(
        ClassNumbers, on_delete=models.SET_NULL, null=True)
