# Generated by Django 4.1.3 on 2022-11-08 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lose',
            fields=[
                ('student_id', models.IntegerField(primary_key=True, serialize=False)),
                ('student_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
