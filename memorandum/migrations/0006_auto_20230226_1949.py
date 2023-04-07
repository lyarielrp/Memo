# Generated by Django 3.2.9 on 2023-02-27 00:49

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('memorandum', '0005_alter_menorandum_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='menorandum',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menorandum',
            name='texto',
            field=ckeditor.fields.RichTextField(),
        ),
    ]