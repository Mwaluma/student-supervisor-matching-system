# Generated by Django 3.1.2 on 2021-01-23 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210122_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='LecturerProfilePicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='profile_pics')),
                ('lecturer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.lecturer')),
            ],
        ),
    ]
