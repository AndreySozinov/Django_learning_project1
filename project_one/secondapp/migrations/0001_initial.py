# Generated by Django 4.2.3 on 2023-07-29 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoinToss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toss', models.CharField(max_length=10)),
                ('toss_time', models.TimeField()),
            ],
        ),
    ]
