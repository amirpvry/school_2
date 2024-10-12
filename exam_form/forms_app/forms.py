from django import forms
from .models import ExamForm
from jalali_date.widgets import AdminJalaliDateWidget  
from jalali_date.fields import JalaliDateField

from django import forms
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime


from django import forms
from .models import ExamForm
from jalali_date.widgets import AdminJalaliDateWidget  
from jalali_date.fields import JalaliDateField

class ExamFormForm(forms.ModelForm):
    class Meta:
        model = ExamForm
        fields = [
            'school_name',
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
            'submitter_name',
            'receiver_name',
            'is_sealed'
        ]
        labels = {
            'school_name': 'نام آموزشگاه',
            'is_sealed': 'وضعیت پلمپ',
            'education_level': 'مقطع تحصیلی',
            'gender': 'جنسیت',
            'reference_number': 'شماره استناد ابلاغ',
            'date_of_reference': 'تاریخ ابلاغ',
            'representative': 'نماینده اداره',
            'date_of_submission': 'تاریخ تحویل نماینده',
            'number_book': 'تعداد دفترها',
            'exam_book_year': 'سال تحصیلی',
            'number_paper_book': 'تعداد صفحات',
            'submission_date': 'تاریخ تحویل نهایی',
            'school_name_2': 'نام مدرسه تحویل‌گیرنده',
            'submitter_name': 'نام و نام خانوادگی تحویل‌دهنده',
            'receiver_name': 'نام و نام خانوادگی تحویل‌گیرنده',
        }

from django import forms
from .models import ExamForm
from django_jalali.forms import jDateField, jDateInput

class SearchForm(forms.Form):
    school_name = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'نام آموزشگاه'
        })
    )

class YearFilterForm(forms.Form):
    year = forms.ChoiceField(
        choices=[
            ('1398-1399', '1398-1399'),
            ('1399-1400', '1399-1400'),
            ('1400-1401', '1400-1401'),
            ('1401-1402', '1401-1402'),
            ('1402-1403', '1402-1403'),
            ('1403-1404', '1403-1404'),
            ('1404-1405', '1404-1405'),
            ('1405-1406', '1405-1406'),
            ('1406-1407', '1406-1407'),
            ('1407-1408', '1407-1408'),
            ('1408-1409', '1408-1409'),
            ('1409-1410', '1409-1410'),
        ],
        required=False,
        label='سال تحصیلی'
    )
class DateFilterForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False, label='از تاریخ')
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False, label='تا تاریخ')

