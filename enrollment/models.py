from django.db import models


class Course(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=30)
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(verbose_name='Дата окончания')
    lectures_count = models.IntegerField(verbose_name='Количество лекций')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=90)
    birth_day = models.DateField(verbose_name='Дата рождения')

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Студент',
                                   related_name='enrolled_student')
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс',
                                  related_name='enrolled_course')
    enrollment_date = models.DateField(verbose_name='Дата зачисления')

    class Meta:
        verbose_name = 'Зачисление'
        verbose_name_plural = 'Зачисления'

    def __str__(self):
        return self.student_id.name
