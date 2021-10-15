# Generated by Django 3.2.8 on 2021-10-15 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('phone_num', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('date_time', models.DateTimeField()),
            ],
        ),
    ]
