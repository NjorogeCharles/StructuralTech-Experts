# Generated by Django 4.2 on 2024-12-04 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StucturalTechExpertsapp', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
