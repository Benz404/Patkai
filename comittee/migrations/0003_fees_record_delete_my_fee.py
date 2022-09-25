# Generated by Django 4.0.4 on 2022-09-23 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comittee', '0002_my_fee_delete_fees_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='fees_record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collected_time', models.DateTimeField(auto_now_add=True)),
                ('student_name', models.CharField(default='', max_length=30)),
                ('roll_number', models.CharField(default='', max_length=8)),
                ('room_number', models.IntegerField(default=0)),
                ('month', models.CharField(default='', max_length=10)),
                ('year', models.IntegerField(default=2022)),
                ('transaction_id', models.CharField(default='', max_length=30)),
                ('mess_dues', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('fine_dues', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total_dues', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name='my_fee',
        ),
    ]
