# Generated by Django 4.1.1 on 2022-10-06 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Surface',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surface', models.CharField(max_length=150)),
                ('infos', models.ManyToManyField(to='main_app.info')),
            ],
        ),
    ]