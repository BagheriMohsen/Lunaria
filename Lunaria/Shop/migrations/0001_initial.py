# Generated by Django 3.0.2 on 2020-01-16 14:46

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='نام محصول')),
                ('slug', models.SlugField(editable=False)),
                ('desc', models.TextField(help_text='توضیحات جزئی برای نمایش یادداشت کنید', verbose_name='توضیحات')),
                ('body', tinymce.models.HTMLField(verbose_name='محتوی')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='تاریخ ویرایش')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
    ]
