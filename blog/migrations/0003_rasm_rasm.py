# Generated by Django 5.1.3 on 2024-11-22 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rasm'),
    ]

    operations = [
        migrations.AddField(
            model_name='rasm',
            name='rasm',
            field=models.ImageField(default=1, upload_to='rasm/'),
            preserve_default=False,
        ),
    ]
