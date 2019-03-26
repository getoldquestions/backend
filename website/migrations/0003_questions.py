# Generated by Django 2.1.4 on 2019-03-26 05:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_contact_date_posted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('level', models.CharField(max_length=75)),
                ('semester', models.CharField(max_length=75)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
