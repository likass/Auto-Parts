# Generated by Django 3.1 on 2020-08-28 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_subcategoryparts_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategoryparts',
            name='price',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
