# Generated by Django 4.2.2 on 2023-07-18 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clicker', '0004_alter_contador_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contador',
            name='data',
            field=models.CharField(blank='true', max_length=100, null='true'),
        ),
    ]