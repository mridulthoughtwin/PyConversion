# Generated by Django 4.0.4 on 2022-05-06 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docum', '0002_userfileupload_document_choices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfileupload',
            name='document_choices',
            field=models.CharField(choices=[('pdftodocs', 'PDF TO DOCX')], max_length=20),
        ),
    ]
