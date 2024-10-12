# Generated by Django 5.0 on 2024-10-12 15:25

import django_jalali.db.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms_app', '0004_examform_is_sealed_alter_examform_date_of_reference_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examform',
            name='date_of_reference',
            field=django_jalali.db.models.jDateField(null=True),
        ),
        migrations.AlterField(
            model_name='examform',
            name='date_of_submission',
            field=django_jalali.db.models.jDateField(null=True, verbose_name='تاریخ تحویل'),
        ),
        migrations.AlterField(
            model_name='examform',
            name='submission_date',
            field=django_jalali.db.models.jDateField(null=True),
        ),
    ]
