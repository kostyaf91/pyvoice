# Generated by Django 3.1 on 2020-09-16 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fillform', '0008_auto_20200911_1136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='logo',
        ),
        migrations.AddField(
            model_name='account',
            name='invoice_count',
            field=models.IntegerField(default=0, max_length=99999, null=True),
        ),
    ]
