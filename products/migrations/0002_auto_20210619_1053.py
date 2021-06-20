# Generated by Django 3.2.3 on 2021-06-19 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'Product Category', 'verbose_name_plural': 'Product Categories'},
        ),
        migrations.AlterModelOptions(
            name='productmanufacturingdetails',
            options={'verbose_name': 'Product Manufacturing Details', 'verbose_name_plural': 'Product Manufacturing Details'},
        ),
        migrations.AlterModelOptions(
            name='productpicture',
            options={'verbose_name': 'Product Picture', 'verbose_name_plural': 'Product Pictures'},
        ),
        migrations.AlterModelOptions(
            name='productspecification',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Product Specifications'},
        ),
        migrations.AlterModelOptions(
            name='productstock',
            options={'verbose_name': 'Product Stock', 'verbose_name_plural': 'Product Inventory'},
        ),
        migrations.AlterModelOptions(
            name='productstockspecification',
            options={'verbose_name': 'Product Stock Specification', 'verbose_name_plural': 'Product Stock Specifications'},
        ),
        migrations.AlterModelOptions(
            name='productsubcategory',
            options={'verbose_name': 'Product SubCategory', 'verbose_name_plural': 'Product SubCategories'},
        ),
    ]