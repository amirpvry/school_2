from django.shortcuts import render, redirect, get_object_or_404
from .forms import ExamFormForm, SearchForm
from .models import ExamForm  # Assuming your model is named ExamForm
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from bidi.algorithm import get_display
import arabic_reshaper
import os
from django.conf import settings
from .forms import DateFilterForm,YearFilterForm

def all_exams_view(request):
    form = YearFilterForm(request.GET or None)
    exams = ExamForm.objects.all()  # گرفتن تمام فرم‌ها به صورت پیش‌فرض

    if form.is_valid():
        selected_year = form.cleaned_data.get('year')  # دریافت سال انتخاب‌شده از فرم

        if selected_year:
            exams = exams.filter(exam_book_year=selected_year)  # فیلتر بر اساس سال تحصیلی

    return render(request, 'all_exams.html', {'exams': exams, 'form': form})

def search_view(request):
    form = SearchForm(request.GET or None)
    results = None
    if form.is_valid():
        school_name = form.cleaned_data.get('school_name')
        results = ExamForm.objects.filter(school_name__icontains=school_name)
    
    return render(request, 'search.html', {'form': form, 'results': results})

def exam_form_view(request):
    if request.method == 'POST':
        form = ExamFormForm(request.POST)
        if form.is_valid():
            form_instance = form.save()
            return redirect('success')  # After saving, redirect to success page
    else:
        form = ExamFormForm()

    return render(request, 'exam_form.html', {'form': form})

def generate_pdf(request, exam_id):
    exam_form = get_object_or_404(ExamForm, id=exam_id)

    # Generate PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="exam_form_{exam_form.school_name}.pdf"'

    # Register the Persian font
    font_path = os.path.join(settings.BASE_DIR, 'B-NAZANIN.TTF')
    pdfmetrics.registerFont(TTFont('BNazanin', font_path))

    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    # Set the font
    p.setFont('BNazanin', 12)

    # Fixed content area (margin remains the same, but content stays within these boundaries)
    margin = 20  # Margins around the edges
    content_width = width - 1.8 * margin  # Keep the content area fixed
    content_height = height - 2 * margin

    # Draw a static border (with fixed size)
    p.setStrokeColorRGB(0, 0, 0)  # Black color
    p.setLineWidth(2)  # Line thickness for the border
    p.rect(margin, margin, content_width, content_height)  # The border remains constant

    # Reshape Persian text correctly
    def draw_persian_text(x, y, text):
        reshaped_text = arabic_reshaper.reshape(text)
        bidi_text = get_display(reshaped_text)
        p.drawRightString(x, y, bidi_text)

    # Set initial y-position based on margin, ensuring the text does not get too close to the borders
    y_position = height - margin - 40  # Starting 40 units below the top margin
    line_spacing = 30  # Vertical space between each line of text

    # Convert 'choices' fields to their display values
    education_level_display = dict(exam_form._meta.get_field('education_level').choices)[exam_form.education_level]
    gender_display = dict(exam_form._meta.get_field('gender').choices)[exam_form.gender]
  # تابع برای تبدیل وضعیت پلمپ به متن
    def get_sealed_status(is_sealed):
        return "پلمپ شده" if is_sealed else "پلمپ نشده"
    # Drawing the dynamic content from the database inside the margin
    p.setFont('BNazanin', 14)  # Set a larger font size for the first line

    # Draw the first line
    draw_persian_text(width - margin, y_position, "         فرم تحویل دفتر امتحانات / فارغ التحصیلان پس از انسداد و پلمپ به آموزشگاه مدیریت آموزش و پرورش شهرستان دشتیاری")
    y_position -= line_spacing  # Move down for the next line

    # Set the font back to normal size for the remaining lines
    p.setFont('BNazanin', 12)  # Reset to normal font size
    draw_persian_text(width - margin, y_position, f" نام آموزشگاه: {exam_form.school_name}     مقطع تحصیلی: {education_level_display}    جنسیت: {gender_display}             وضعیت پلمپ: {get_sealed_status(exam_form.is_sealed)}")
    y_position -= line_spacing
    # draw_persian_text(width - margin, y_position, f"مقطع تحصیلی: {education_level_display}")
    # y_position -= line_spacing
    # draw_persian_text(width - margin, y_position, f"جنسیت: {gender_display}")
    # y_position -= line_spacing
    draw_persian_text(width - margin, y_position, f" با احترام به استناد ابلاغ شماره: {exam_form.reference_number}   مورخ: {exam_form.date_of_reference}   توسط نماینده اداره برادر / خواهر: {exam_form.representative}  در تاریخ: {exam_form.date_of_submission}")
    y_position -= line_spacing
    # draw_persian_text(width - margin, y_position, f" مورخ: {exam_form.date_of_reference}")
    # y_position -= line_spacing
    # draw_persian_text(width - margin, y_position, f" توسط نماینده اداره برادر / خواهر: {exam_form.representative}")
    # y_position -= line_spacing
    draw_persian_text(width - margin, y_position, f" در تاریخ: {exam_form.date_of_submission} تعداد : {exam_form.number_book} دفتر امتحانات حاوی: {exam_form.number_paper_book} صفحه مربوط به سال تحصیلی {exam_form.exam_book_year} انسداد گردید.")
    y_position -= line_spacing
    # draw_persian_text(width - margin, y_position, f" تعداد : {exam_form.number_book} دفتر امتحانات حاوی: {exam_form.number_paper_book} صفحه مربوط به سال تحصیلی {exam_form.date_of_submission} انسداد گردید" )
    # y_position -= line_spacing
    # draw_persian_text(width - margin, y_position, f"مربوط به سال تحصیلی {exam_form.date_of_submission} انسداد گردید")

    # y_position -= line_spacing
    draw_persian_text(width - margin, y_position, f" و در تاریخ{exam_form.submission_date} پس ازپلمپ توسط کارشناسی سنجش و ارزشیابی تحصیلی تحویل مدیر / معاون  آموزشگاه برادر / خواهر  {exam_form.school_name_2}  گردید.")

    y_position -= line_spacing
    # draw_persian_text(width - margin, y_position, f"  آموزشگاه برادر / خواهر  {exam_form.school_name_2}  گردید.   ")

    # y_position -= line_spacing

    draw_persian_text(width - margin, y_position, f" نام و نام خانوادگی تحویل دهنده: {exam_form.submitter_name}               نام و نام خانوادگی تحویل گیرنده: {exam_form.receiver_name}")
    y_position -= line_spacing


    draw_persian_text(width - margin, y_position, " مهر و امضا                                                  مهر و امضا" )
    y_position -= line_spacing

    # Save the PDF
    p.showPage()
    p.save()

    return response



def success_view(request):
    return render(request, 'success.html')
