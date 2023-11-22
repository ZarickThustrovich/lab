# Generated by Django 4.2.7 on 2023-11-22 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_sessionchathistory'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sessions',
            new_name='Session',
        ),
        migrations.RenameField(
            model_name='sessionchathistory',
            old_name='session_uuid',
            new_name='session',
        ),
        migrations.AddField(
            model_name='sessionchathistory',
            name='message',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]