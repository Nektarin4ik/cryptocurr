# Generated by Django 3.2.15 on 2023-03-23 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0002_auto_20230323_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptocurrency',
            name='name',
            field=models.CharField(max_length=256),
        ),
    ]