# Generated by Django 4.1.1 on 2022-09-20 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students_detail',
            name='room_number',
            field=models.IntegerField(default=0),
        ),
    ]
