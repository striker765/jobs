# Generated by Django 5.1.1 on 2024-10-06 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_cc_fast_criticidade_alter_cc_fast_datacenter_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cc_fast',
        ),
        migrations.DeleteModel(
            name='Cc_server',
        ),
    ]
