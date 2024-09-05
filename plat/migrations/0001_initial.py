# Generated by Django 5.1.1 on 2024-09-05 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlatModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('summary', models.TextField()),
            ],
            options={
                'verbose_name': 'Plat',
                'verbose_name_plural': 'Plats',
            },
        ),
    ]
