# Generated by Django 3.2.9 on 2023-02-20 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('members', '0004_auto_20230220_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='joined_date',
        ),
        migrations.RemoveField(
            model_name='member',
            name='phone',
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]