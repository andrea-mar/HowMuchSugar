# Generated by Django 3.2.4 on 2021-06-15 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sugarList', '0003_alter_product_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productImage',
            field=models.ImageField(upload_to='img'),
        ),
        migrations.AlterField(
            model_name='product',
            name='productSugar',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
