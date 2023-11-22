# Generated by Django 4.2.7 on 2023-11-22 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_sessions'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionChatHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=255)),
                ('session_uuid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.sessions')),
            ],
            options={
                'verbose_name': 'Отправитель',
                'verbose_name_plural': 'Отправители',
            },
        ),
    ]
