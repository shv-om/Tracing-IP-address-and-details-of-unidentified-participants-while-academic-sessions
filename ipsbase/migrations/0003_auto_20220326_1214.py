# Generated by Django 3.2.4 on 2022-03-26 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipsbase', '0002_auto_20220326_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='randomid',
            name='ruser',
        ),
        migrations.DeleteModel(
            name='IPaddress',
        ),
        migrations.DeleteModel(
            name='RandomID',
        ),
    ]
