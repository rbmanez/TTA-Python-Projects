# Generated by Django 2.0.7 on 2019-08-16 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190813_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('drinks', 'drinks'), ('treats', 'treats'), ('entrees', 'entrees'), ('appetizers', 'appetizers')], max_length=60),
        ),
    ]