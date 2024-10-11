from django.db import models

class ExamForm(models.Model):
    school_name = models.CharField(max_length=255)
    education_level = models.CharField(max_length=100, choices=[
        ('primary_first', 'ابتدایی دوره اول'),
        ('primary_second', 'ابتدایی دوره دوم'),
        ('middle_school', 'متوسطه دوره اول'),
        ('high_school', 'متوسطه دوره دوم'),
    ])
    gender = models.CharField(max_length=10, choices=[
        ('boy', 'پسرانه'),
        ('girl', 'دخترانه'),
        ('mixed', 'مختلط'),
    ])
    reference_number = models.CharField(max_length=100 , null=True)  # شماره استناد ابلاغ
    date_of_reference = models.DateField(null=True)  # تاریخ ابلاغ (حالا نال‌پذیر)
    representative = models.CharField(max_length=255 , null=True)  # نماینده اداره
    date_of_submission = models.DateField(null=True)  # تاریخ تحویل (حالا نال‌پذیر)
    exam_book_year = models.CharField(max_length=100, null=True)  # سال تحصیلی (حالا نال‌پذیر)
    submission_date = models.DateField(null=True)  # تاریخ تحویل
    submitter_name = models.CharField(max_length=255, null=True)  # نام و نام خانوادگی تحویل‌دهنده (حالا نال‌پذیر)
    receiver_name = models.CharField(max_length=255, null=True)  # نام و نام خانوادگی تحویل‌گیرنده

    def __str__(self):
        return f"{self.school_name} - {self.education_level} - {self.gender}"
