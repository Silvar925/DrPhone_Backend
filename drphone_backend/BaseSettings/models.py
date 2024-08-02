from django.db import models


class ColorProduct(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название цвета')
    codeColor = models.CharField(max_length=30, verbose_name='Код цвета HEX/RGB/RGBa')

    class Meta:
        verbose_name = "Цвет товара"
        verbose_name_plural = "Цвет товаров"

    def __str__(self) -> str:
        return f"{self.name}"

class ImagesProduct(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название изображения')
    image = models.ImageField(upload_to='media/ProductImages/', verbose_name="Изображение")

    class Meta:
        verbose_name = "Изображение товара"
        verbose_name_plural = "Изображения товаров"

    def __str__(self) -> str:
        return f"{self.name}"

class MemoryProducts(models.Model):
    size = models.CharField(max_length=30, verbose_name='Объем памяти')

    class Meta:
        verbose_name = "Память"
        verbose_name_plural = "Памяти"

    def __str__(self) -> str:
        return f"{self.size}"


class SIMProduct(models.Model):
    type = models.CharField(max_length=30, verbose_name='Тип SIM карты')

    class Meta:
        verbose_name = "Симкарта"
        verbose_name_plural = "Симкарты"

    def __str__(self) -> str:
        return f"{self.type}"


class Manufacturer(models.Model):
    name = models.CharField(max_length=30, verbose_name="Производитель")
    
    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"

    def __str__(self) -> str:
        return f"{self.name}"
    

class RAM(models.Model):
    size = models.CharField(max_length=30, verbose_name='Объем памяти')

    class Meta:
        verbose_name = "Оперативная память"
        verbose_name_plural = "Оперативные памяти"

    def __str__(self) -> str:
        return f"{self.size}"
