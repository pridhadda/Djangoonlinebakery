# Generated by Django 2.0.3 on 2018-03-25 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_prod_del_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prod',
            name='del_date',
        ),
        migrations.AddField(
            model_name='prod',
            name='detail',
            field=models.TextField(blank=True),
        ),
    ]