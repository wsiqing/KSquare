# Generated by Django 2.1.3 on 2018-11-20 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge', '0003_auto_20181120_0337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forthrelationentry',
            name='to_partner_relation',
        ),
        migrations.AddField(
            model_name='forthrelationentry',
            name='to_relation_partner',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='forth_relation_partner', to='knowledge.ToRelationEntry'),
        ),
    ]
