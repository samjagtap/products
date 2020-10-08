# Generated by Django 2.2.3 on 2020-10-08 11:19

from django.db import migrations, models
import prodapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('cost_per_item', models.FloatField(default=0, validators=[prodapp.models.cost_value_greater_than_zero])),
                ('stock_quantity', models.PositiveIntegerField(default=0)),
                ('volume', models.FloatField(default=0)),
            ],
            options={
                'db_table': 'Products',
            },
        ),
    ]
