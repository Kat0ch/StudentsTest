from django.db import models


class Course(models.Model):
    name: models.CharField = models.CharField(verbose_name='Имя', max_length=30)
    start_date: models.DateField = models.DateField(verbose_name='Дата начала')
    end_date: models.DateField = models.DateField(verbose_name='Дата окончания')
    lectures_count: models.IntegerField = models.IntegerField(verbose_name='Количество лекций')

    class Meta:
        verbose_name: str = 'Курс'
        verbose_name_plural: str = 'Курсы'

    def __str__(self):
        return self.name


class Student(models.Model):
    name: models.CharField = models.CharField(verbose_name='Имя', max_length=90)
    birth_day: models.DateField = models.DateField(verbose_name='Дата рождения')

    class Meta:
        verbose_name: str = 'Студент'
        verbose_name_plural: str = 'Студенты'

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    # FIXME: student_id и course_id - плохое название для полей.
    #  должно быть student и course, а student_id и course_id джанга генерит сама и там будет int (PK из Student и Course)
    #  а student - это объект Student
    student_id: models.ForeignKey = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Студент',
                                                      related_name='enrolled_student')
    course_id: models.ForeignKey = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс',
                                                     related_name='enrolled_course')
    enrollment_date: models.DateField = models.DateField(verbose_name='Дата зачисления')

    class Meta:
        verbose_name: str = 'Зачисление'
        verbose_name_plural: str = 'Зачисления'

    def __str__(self):
        return self.student_id.name
