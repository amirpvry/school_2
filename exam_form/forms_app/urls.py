from django.urls import path
from .views import *

urlpatterns = [
    path('', exam_form_view, name='exam_form'),
    path('success/', success_view, name='success'),
    path('search/', search_view, name='search'),
    path('generate_pdf/<int:exam_id>/', generate_pdf, name='generate_pdf'),
    path('all_exams/', all_exams_view, name='all_exams'),


]
