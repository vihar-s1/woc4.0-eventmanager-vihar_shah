# Generated by Django 4.0.1 on 2022-01-19 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventName', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
