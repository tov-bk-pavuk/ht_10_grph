# Generated by Django 3.2.7 on 2021-09-03 01:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='logistics.supplier'),
        ),
    ]
