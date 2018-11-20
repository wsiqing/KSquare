# Generated by Django 2.1.3 on 2018-11-20 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge', '0004_auto_20181120_0354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forthrelationentry',
            name='related_concept',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relation_forth', to='knowledge.Concept'),
        ),
        migrations.AlterField(
            model_name='torelationentry',
            name='related_concept',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relation_to', to='knowledge.Concept'),
        ),
    ]
