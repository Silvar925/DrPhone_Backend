from django.db import models
from BaseSettings.models import ColorProduct, ImagesProduct, MemoryProducts, SIMProduct, Manufacturer
from transliterate import translit


class Phones(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Производитель")
    name = models.CharField(max_length=50, verbose_name='Название товара')

    allColors = models.ManyToManyField(ColorProduct, verbose_name="Цвета товара", related_name='all_colors_phone')
    allMemory = models.ManyToManyField(MemoryProducts, verbose_name="Память", related_name='all_memory_phone')
    allSim = models.ManyToManyField(SIMProduct, verbose_name="Тип симкарты", related_name="all_SIM_phone")

    class Meta:
        verbose_name = "Телефон"
        verbose_name_plural = "Телефоны"

    def __str__(self) -> str:
        return f"{self.manufacturer}-{self.name}"


class PhonesOptions(models.Model):
    unique_id = models.CharField(max_length=200, unique=True, blank=True, null=True, verbose_name='Уникальный ID')
    phone = models.ForeignKey(Phones, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Устройство")
    
    color = models.ForeignKey(ColorProduct, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Цвет")
    memory = models.ForeignKey(MemoryProducts, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Память")
    sim = models.ForeignKey(SIMProduct, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Тип сим-карты")

    images = models.ManyToManyField(ImagesProduct, verbose_name="Изображение", related_name='images_phone_options')
    used = models.BooleanField(default=False, verbose_name="Подержанный")
    discountedPrice = models.IntegerField(verbose_name='Цена со скидкой', blank=True, null=True)

    count = models.IntegerField(verbose_name="Количество: ", blank=True, null=True)
    price = models.IntegerField(verbose_name="Цена", blank=True, null=True)

    def save(self, *args, **kwargs):
        # Генерация транслита с удалением плюса
        name_translit = translit(str(self.phone), 'ru', reversed=True).replace(' ', '-').replace('+', '') if self.phone else ''
        color_translit = translit(self.color.name, 'ru', reversed=True).replace(' ', '-').replace('+', '') if self.color else ''
        memory_translit = translit(self.memory.size, 'ru', reversed=True).replace(' ', '-').replace('+', '') if self.memory else ''
        sim_translit = translit(self.sim.type, 'ru', reversed=True).replace(' ', '-').replace('+', '') if self.sim else ''
        used_translit = 'used' if self.used else 'new'
        
        # Создание уникального ID
        self.unique_id = f"{name_translit}-{color_translit}-{memory_translit}-{sim_translit}-{used_translit}"

        super(PhonesOptions, self).save(*args, **kwargs)


    class Meta:
        verbose_name = "Вариант телефона"
        verbose_name = "Варианты телефона"

    def __str__(self) -> str:
        return f"{self.phone}-{self.color}-{self.memory}-{self.sim}"


class Accessories(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название товара')
    allColors = models.ManyToManyField(ColorProduct, verbose_name="Цвет")
    
    allMemory = models.ManyToManyField(MemoryProducts, verbose_name='Память')
    images = models.ManyToManyField(ImagesProduct, verbose_name="Изображение")
    price = models.IntegerField(verbose_name="Цена", blank=True, null=True)

    class Meta:
        verbose_name = "Аксессуар"
        verbose_name_plural = "Аксессуары"

    def __str__(self) -> str:
        # colors = ', '.join([color.name for color in self.allColors.all()])
        return f"{self.name}"


class AccessoriesOptions(models.Model):
    accessories = models.ForeignKey(Accessories, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Аксессуар")

    color = models.ForeignKey(ColorProduct, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Цвет")
    memory = models.ForeignKey(MemoryProducts, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Память")
    sim = models.ForeignKey(SIMProduct, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Тип сим-карты")
    used = models.BooleanField(default=False, verbose_name="Подержанный")

    def save(self, *args, **kwargs):
        # Генерация транслита с удалением плюса
        name_translit = translit(str(self.accessories), 'ru', reversed=True).replace(' ', '-').replace('+', '') if self.accessories else ''
        color_translit = translit(self.color.name, 'ru', reversed=True).replace(' ', '-').replace('+', '') if self.color else ''
        memory_translit = translit(self.memory.size, 'ru', reversed=True).replace(' ', '-').replace('+', '') if self.memory else ''
        sim_translit = translit(self.sim.type, 'ru', reversed=True).replace(' ', '-').replace('+', '') if self.sim else ''
        used_translit = 'used' if self.used else 'new'
        
        # Создание уникального ID
        self.unique_id = f"{name_translit}-{color_translit}-{memory_translit}-{sim_translit}-{used_translit}"

        super(AccessoriesOptions, self).save(*args, **kwargs)



    class Meta:
        verbose_name = "Вариант аксессуара"
        verbose_name_plural = "Варианты аксессуаров"

    def __str__(self) -> str:
        return f"{self.accessories}-{self.color}-{self.memory}-{self.sim}-{self.used}"


class Covers(models.Model):
    unique_id = models.SlugField(max_length=255, unique=True, editable=False)
    name = models.CharField(max_length=50, verbose_name='Название товара')
    color = models.ManyToManyField(ColorProduct, verbose_name="Цвет")
    images = models.ManyToManyField(ImagesProduct, verbose_name="Изображение")
    price = models.IntegerField(verbose_name="Цена", blank=True, null=True)

    class Meta:
        verbose_name = "Чехол"
        verbose_name_plural = "Чехлы"

    def __str__(self) -> str:
        return f"{self.name}-{self.color}"


class IMac(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название товара')
    
    allColors = models.ManyToManyField(ColorProduct, verbose_name="Цвета iMac", related_name='all_device_imac')
    allMemory = models.ManyToManyField(MemoryProducts, verbose_name="Память", related_name='all_memory_imac')

    class Meta:
        verbose_name = "iMac"
        verbose_name_plural = "iMac'и"

    def __str__(self) -> str:
        return f"{self.name}"
    

class IMacOptions(models.Model):
    unique_id = models.CharField(max_length=200, unique=True, blank=True, null=True, verbose_name='Уникальный ID')
    imac = models.ForeignKey(IMac, verbose_name="iMac", on_delete=models.SET_NULL, null=True, blank=True)

    color = models.ForeignKey(ColorProduct, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Цвет")
    memory = models.ForeignKey(MemoryProducts, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Память")
    images = models.ManyToManyField(ImagesProduct, verbose_name="Изображение", related_name='all_images_imac_options')
    
    used = models.BooleanField(default=False, verbose_name="Подержанный")
    price = models.IntegerField(verbose_name="Цена", blank=True, null=True)

    def save(self, *args, **kwargs):
        # Генерация транслита с удалением плюса
        name_translit = translit(str(self.imac), 'ru', reversed=True).replace(' ', '-').replace('+', '') if self.imac else ''
        color_translit = translit(self.color.name, 'ru', reversed=True).replace(' ', '-').replace('+', '') if self.color else ''
        memory_translit = translit(self.memory.size, 'ru', reversed=True).replace(' ', '-').replace('+', '') if self.memory else ''
        used_translit = 'used' if self.used else 'new'
        
        # Создание уникального ID
        self.unique_id = f"{name_translit}-{color_translit}-{memory_translit}-{used_translit}"

        super(IMacOptions, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Вариант IMac"
        verbose_name_plural = "Варианты IMac'ов"

    def __str__(self) -> str:
        return f"{self.imac}-{self.color}-{self.memory}"
    

# filter_horizontal