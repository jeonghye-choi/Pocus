# Generated by Django 3.2.4 on 2021-06-23 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.CharField(max_length=16, unique=True)),
                ('user_pw', models.CharField(max_length=32)),
                ('user_name', models.CharField(max_length=16)),
                ('user_stuid', models.CharField(max_length=9)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
