# Generated by Django 5.0.2 on 2024-02-19 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0002_register_is_admin_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english', models.CharField(max_length=5)),
                ('maths', models.CharField(max_length=5)),
                ('science', models.CharField(max_length=5)),
            ],
        ),
    ]
