# Generated by Django 2.1.3 on 2018-11-20 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge', '0002_auto_20181120_0335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forthrelationentry',
            name='related_concept',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='forth_relation', to='knowledge.Concept'),
        ),
    ]
