# Generated by Django 3.2.3 on 2021-05-15 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_order_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='menu',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='table',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tablebooking',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
