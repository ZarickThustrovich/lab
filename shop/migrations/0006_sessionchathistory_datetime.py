# Generated by Django 4.2.7 on 2023-11-22 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_rename_sessions_session_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessionchathistory',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
