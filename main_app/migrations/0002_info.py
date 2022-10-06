# Generated by Django 4.1.1 on 2022-10-06 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namesake', models.CharField(max_length=150)),
                ('years', models.IntegerField(default=0)),
                ('planet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moons', to='main_app.planet')),
            ],
        ),
    ]
