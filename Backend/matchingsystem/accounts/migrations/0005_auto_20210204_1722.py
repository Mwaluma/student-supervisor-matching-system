# Generated by Django 3.1.2 on 2021-02-04 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_auto_20210123_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='lecturer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='lecturerprofilepicture',
            name='picture',
            field=models.ImageField(blank=True, upload_to='profile_pics/'),
        ),
    ]