# Generated by Django 2.1.3 on 2018-11-21 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge', '0009_auto_20181121_0735'),
    ]

    operations = [
        migrations.RenameField(
            model_name='concept',
            old_name='title',
            new_name='_title',
        ),
        migrations.RenameField(
            model_name='relation',
            old_name='title',
            new_name='_title',
        ),
    ]
