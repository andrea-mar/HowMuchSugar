# Generated by Django 3.2.4 on 2021-06-07 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sugarList', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productImage',
            field=models.ImageField(upload_to='static/sugarList/img'),
        ),
    ]