from django import forms
from .models import ExamForm


class ExamFormForm(forms.ModelForm):
    class Meta:
        model = ExamForm
        fields = ['school_name',
                  'education_level',
                  'gender', 
                  'reference_number', 
                  'date_of_reference',
                  'representative',
                  'date_of_submission',
                  'exam_book_year',
                  'number_book',
                  'number_paper_book',
                  'submission_date',
                  'school_name_2',
                  'submitter_name' ,
                  'receiver_name',
                  'is_sealed'
                  
                  
                  
                  ]
        labels = {
            'school_name': 'نام آموزشگاه',
            'is_sealed' : 'وضعیت پلمپ',
            'education_level': 'مقطع تحصیلی',
            'gender': 'جنسیت',
            'reference_number': 'شماره استناد ابلاغ',
            'date_of_reference': 'تاریخ ابلاغ',
            'representative': 'نماینده اداره',
            'date_of_submission': 'تاریخ تحویل نماینده',
            'number_book': 'تعداد دفتر ها',
            'exam_book_year': ' سال تحصیلی ',
            'number_paper_book': 'تعداد صفحات',
            'submission_date': 'تاریخ تحویل',
            'school_name_2' : 'نام مدرسه تحویل  گیرنده',
            'submitter_name': 'نام و نام خانوادگی تحویل‌دهنده',
            'receiver_name': 'نام و نام خانوادگی تحویل‌گیرنده',
        }

class SearchForm(forms.Form):
    school_name = forms.CharField(max_length=100, required=False, label='نام آموزشگاه')
