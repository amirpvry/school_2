from django.db import models

class ExamForm(models.Model):
    school_name = models.CharField(max_length=255, verbose_name='نام آموزشگاه')
    
    education_level = models.CharField(
        max_length=100, 
        choices=[
            ('primary_first', 'ابتدایی دوره اول'),
            ('primary_second', 'ابتدایی دوره دوم'),
            ('middle_school', 'متوسطه دوره اول'),
            ('high_school', 'متوسطه دوره دوم'),
        ], 
        verbose_name='مقطع تحصیلی'
    )
    
    gender = models.CharField(
        max_length=10, 
        choices=[
            ('boy', 'پسرانه'),
            ('girl', 'دخترانه'),
            ('mixed', 'مختلط'),
        ], 
        verbose_name='جنسیت'
    )
    
    reference_number = models.CharField(max_length=100, null=True, verbose_name='شماره استناد ابلاغ')  # شماره استناد ابلاغ
    date_of_reference = models.DateField(null=True, verbose_name='تاریخ ابلاغ')  # تاریخ ابلاغ
    
    representative = models.CharField(max_length=255, null=True, verbose_name='نماینده اداره')  # نماینده اداره
    date_of_submission = models.DateField(null=True, verbose_name='تاریخ تحویل')  # تاریخ تحویل
    
    exam_book_year = models.CharField(max_length=100, null=True, verbose_name='سال تحصیلی')  # سال تحصیلی
    number_book = models.IntegerField(null=True, verbose_name='تعداد دفتر امتحانات')  # تعداد دفتر
    number_paper_book = models.IntegerField(null=True, verbose_name='تعداد صفحات دفتر')  # تعداد صفحات دفتر
    
    submission_date = models.DateField(null=True, verbose_name='تاریخ تحویل نهایی')  # تاریخ تحویل نهایی
    
    school_name_2 = models.CharField(max_length=256, null=True, verbose_name='نام آموزشگاه (دومین نام)')  # نام آموزشگاه دوم (در صورت وجود)

    submitter_name = models.CharField(max_length=255, null=True, verbose_name='نام و نام خانوادگی تحویل‌دهنده')  # نام و نام خانوادگی تحویل‌دهنده
    receiver_name = models.CharField(max_length=255, null=True, verbose_name='نام و نام خانوادگی تحویل‌گیرنده')  # نام و نام خانوادگی تحویل‌گیرنده
    
    is_sealed = models.BooleanField(default=False, verbose_name='وضعیت پلمپ')  # وضعیت پلمپ (جدید)

    def __str__(self):
        return f"{self.school_name} - {self.education_level} - {self.gender}"
