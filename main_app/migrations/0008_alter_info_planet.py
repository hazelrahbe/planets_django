# Generated by Django 4.1.1 on 2022-10-06 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_info_planet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='planet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moons', to='main_app.planet'),
        ),
    ]