# Generated by Django 2.1.1 on 2018-09-09 07:22

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Identification Number')),
                ('full_name', models.CharField(max_length=100)),
                ('face_id', models.CharField(blank=True, max_length=250)),
            ],
        ),
    ]