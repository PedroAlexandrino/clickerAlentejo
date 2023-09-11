# Generated by Django 4.2.2 on 2023-06-13 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contador', models.CharField(max_length=100)),
                ('data', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='P1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p1', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='P2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p2', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='P3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p3', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta', models.CharField(max_length=250)),
                ('data', models.CharField(max_length=100)),
            ],
        ),
    ]
