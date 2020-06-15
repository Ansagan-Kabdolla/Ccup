from django.db import models
import json
from django.db import models



class Zakaz(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    email = models.EmailField(verbose_name='Email')
    date = models.DateField(verbose_name='Date')
    number = models.IntegerField(verbose_name='Number')
    table_number = (
        ('Table 1', 'Table 1'),
        ('Table 2', 'Table 2'),
        ('Table 3', 'Table 3'),
        ('Table 4', 'Table 4'),
        ('Table 5', 'Table 5'),
        ('Table 6', 'Table 6'),
    )
    table = models.CharField(max_length=7,choices=table_number, default='Table 1',verbose_name='Table')
    foods = models.ManyToManyField('Food')

    def get_foods(self):
        return "\n".join([p.name for p in self.foods.all()])
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Food(models.Model):
    name = models.CharField(max_length=100,verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    image = models.FileField(upload_to='FoodImage',verbose_name='Composition')
    composition = models.TextField(verbose_name='Composition')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    category = models.ForeignKey('Category',on_delete=models.CASCADE,verbose_name='Category')
    def __str__(self):
        new_food = {
            "id": str(self.pk),
            "title": self.name,
            "price": str(self.price),
                }
        with open("restoran/static/restoran/js/data_file.json") as read_file:
            try:
                z = False
                data = json.load(read_file)
            except:
                z = True
                data = {
                    "basket":[new_food]
                }
        with open("restoran/static/restoran/js/data_file.json", "w") as f:
            if z==False:
                data["basket"].append(new_food)
            json.dump(data, f)
        return self.name
    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'


class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name='Name')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'