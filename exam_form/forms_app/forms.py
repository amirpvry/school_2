from django import forms
from .models import ExamForm


class ExamFormForm(forms.ModelForm):
    class Meta:
        model = ExamForm  # یا نام مدل شما
        fields = [
            'school_name',
            'education_level',
            'gender',
            'reference_number',  # شماره استناد ابلاغ
            'date_of_reference',  # تاریخ ابلاغ
            'representative',  # نماینده اداره
            'date_of_submission',  # تاریخ تحویل
            'exam_book_year',  # سال تحصیلی
            'submission_date',  # تاریخ تحویل
            'submitter_name',  # نام و نام خانوادگی تحویل‌دهنده
            'receiver_name',  # نام و نام خانوادگی تحویل‌گیرنده
        ]
class SearchForm(forms.Form):
    school_name = forms.CharField(max_length=100, required=False, label='نام آموزشگاه')
