# Generated by Django 3.1 on 2020-09-16 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fillform', '0010_auto_20200916_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='invoice_count',
            field=models.IntegerField(default='00000', null=True),
        ),
    ]
