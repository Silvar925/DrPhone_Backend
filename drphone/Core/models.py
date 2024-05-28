from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название продукта')
    images = models.ManyToManyField('ProductImage', verbose_name='Изображения продукта', blank=True)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_images/', verbose_name='Изображение')

    def __str__(self):
        return f"Image {self.id}"



class Service(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название услуги')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.name


class ProductOption(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    color = models.CharField(max_length=50, verbose_name='Цвета')
    memory = models.IntegerField(verbose_name='Объем памяти в гб')  # Объем памяти в ГБ
    sim_type = models.CharField(max_length=50, verbose_name='Тип симкарты')

    def __str__(self):
        return f"{self.product.name} - {self.color}, {self.memory}GB, {self.sim_type}"


class ProductPrice(models.Model):
    product_option = models.ForeignKey(ProductOption, on_delete=models.CASCADE, verbose_name='Варианты продукта')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена продукта')

    def __str__(self):
        return f"{self.product_option} - {self.price}"
