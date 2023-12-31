# Generated by Django 4.1 on 2023-09-24 16:31

import django.core.validators
from django.db import migrations, models
import upload.validators


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='', validators=[upload.validators.MaxFileSizeValidator(102400), django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'webp', 'txt'])]),
        ),
    ]
