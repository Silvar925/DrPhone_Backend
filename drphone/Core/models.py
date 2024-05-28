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
    name = models.CharField(max_length=30, verbose_name='Название изображения')
    photo = models.ImageField(upload_to='media/ProductImages/', verbose_name="Изображение")

    class Meta:
        verbose_name = "Изображение товара"
        verbose_name_plural = "Изображения товаров"

    def __str__(self) -> str:
        return f"{self.name}"


class Product(models.Model):
    SIM_CHOICES = [
        ('SIM_SIM', 'SIM + SIM'),
        ('ESIM_SIM', 'ESIM + SIM'),
        ('ESIM_ONLY', 'ESIM ONLY'),
    ]

    MEMORY_CHOICES = [
        ('128Gb','128Gb'),
        ('256Gb','256Gb'),
        ('512Gb','512Gb'),
        ('1024Gb','1024Gb'),
        ('2048Gb','2048Gb'),
    ]

    name = models.CharField(max_length=50, verbose_name='Название товара')
    color = models.ManyToManyField(ColorProduct, verbose_name="Цвет")
    memory = models.CharField(max_length=8, choices=MEMORY_CHOICES, blank=True, null=True, verbose_name='Память')
    images = models.ManyToManyField(ImagesProduct, verbose_name="Изображение")
    sim = models.CharField(max_length=20, choices=SIM_CHOICES, blank=True, null=True, verbose_name='СИМ КАРТА')
    price = models.IntegerField(verbose_name="Цена", blank=True, null=True)


    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self) -> str:
        return f"{self.name} {self.color} {self.memory} {self.sim}"