# Generated by Django 4.0.5 on 2022-07-10 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mcm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producttype',
            name='created_by',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductType',
        ),
    ]
