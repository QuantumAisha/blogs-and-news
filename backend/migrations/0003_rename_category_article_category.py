# Generated by Django 4.2.7 on 2023-11-08 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_article_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='Category',
            new_name='category',
        ),
    ]
