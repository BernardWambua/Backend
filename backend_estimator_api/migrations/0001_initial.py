# Generated by Django 3.0.5 on 2020-04-13 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('http_method', models.CharField(max_length=10)),
                ('request_path', models.CharField(max_length=50)),
                ('request_status', models.CharField(max_length=20)),
                ('request_time', models.CharField(max_length=10)),
            ],
        ),
    ]
