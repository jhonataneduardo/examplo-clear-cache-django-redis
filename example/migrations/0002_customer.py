# Generated by Django 3.2.8 on 2021-10-10 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80, verbose_name='Name')),
                ('last_name', models.CharField(max_length=80, verbose_name='Name')),
            ],
        ),
    ]