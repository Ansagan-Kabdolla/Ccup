# Generated by Django 3.0.5 on 2020-06-13 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restoran', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Price'),
        ),
    ]