# Generated by Django 3.2.4 on 2022-03-24 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ipsbase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentid',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
