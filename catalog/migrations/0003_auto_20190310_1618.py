# Generated by Django 2.1.5 on 2019-03-10 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20190310_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='reorder_trigger',
            field=models.IntegerField(null=True),
        ),
    ]