# Generated by Django 5.1.3 on 2024-11-22 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rasm_rasm'),
    ]

    operations = [
        migrations.CreateModel(
            name='Haridor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=50)),
                ('rasm', models.ImageField(upload_to='haridor/')),
                ('bio', models.TextField()),
            ],
        ),
    ]
