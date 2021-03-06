# Generated by Django 2.1 on 2019-04-11 11:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20190404_1312'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sName', models.CharField(max_length=75)),
                ('level', models.CharField(max_length=75)),
                ('faculty', models.CharField(max_length=75)),
                ('semester', models.IntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='questionfiles',
            name='sname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Subject'),
        ),
    ]
