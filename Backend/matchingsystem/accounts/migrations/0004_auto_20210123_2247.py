# Generated by Django 3.1.2 on 2021-01-23 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_lecturerprofilepicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturerprofilepicture',
            name='picture',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
    ]
