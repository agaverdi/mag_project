# Generated by Django 3.0 on 2020-03-28 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magapp', '0006_auto_20200328_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_comments',
        ),
    ]
