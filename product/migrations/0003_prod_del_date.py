# Generated by Django 2.0.3 on 2018-03-16 13:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_prod_add_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='prod',
            name='del_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 16, 13, 34, 55, 977926, tzinfo=utc)),
        ),
    ]
