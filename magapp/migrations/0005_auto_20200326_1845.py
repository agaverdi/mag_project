# Generated by Django 3.0 on 2020-03-26 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magapp', '0004_auto_20200326_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='reply_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replycomments', to='magapp.Comments'),
        ),
    ]
