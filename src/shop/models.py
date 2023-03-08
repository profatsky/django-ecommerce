from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=60, verbose_name='Название')
    slug = models.SlugField(max_length=80, unique=True, db_index=True, verbose_name='URL')

    class Meta:
        ordering = ('title',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(max_length=60, verbose_name='Название')
    slug = models.SlugField(max_length=80, unique=True, db_index=True, verbose_name='URL')

    class Meta:
        ordering = ('title',)
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey('Category', related_name='products', on_delete=models.PROTECT,
                                 verbose_name='Категория')
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.CASCADE, verbose_name='Бренд')
    slug = models.SlugField(max_length=200, unique=True, blank=True, db_index=True, verbose_name='URL')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
                                         verbose_name='Цена со скидкой')
    units = models.PositiveIntegerField(default=0, verbose_name='Кол-во')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Время обновления')

    class Meta:
        abstract = True
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'category_slug': self.category.slug, 'product_slug': self.slug})

    def get_specification_url(self):
        return reverse('product_specification', kwargs={'category_slug': self.category.slug, 'product_slug': self.slug})


class Smartphone(Product):
    # Заводские данные
    guarantee = models.PositiveSmallIntegerField(blank=True, verbose_name='Гарантия')
    manufacturer_country = models.ForeignKey('ManufacturerCountry', related_name='smartphones',
                                             on_delete=models.PROTECT, verbose_name='Страна производитель')

    # Серия модели
    series = models.CharField(max_length=30, blank=True, verbose_name='Серия')
    model = models.CharField(max_length=30, blank=True, verbose_name='Модель')

    # Операционная система
    operating_system = models.ForeignKey('OperatingSystem', related_name='smartphones',
                                         on_delete=models.PROTECT, verbose_name='Операционная система')

    # Экран
    screen_diagonal = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Диагональ экрана в дюймах')
    screen_resolution_vertical = models.PositiveSmallIntegerField(verbose_name='Разрешение экрана по вертикали')
    screen_resolution_horizontal = models.PositiveSmallIntegerField(verbose_name='Разрешение экрана по горизонтали')
    screen_technology = models.ForeignKey('ScreenTechnology', related_name='smartphones', on_delete=models.PROTECT,
                                          verbose_name='Технология экрана')
    screen_refresh_rate = models.ForeignKey('ScreenRefreshRate', related_name='smartphones', on_delete=models.PROTECT,
                                            verbose_name='Частота обновления экрана (Гц)')

    # Процессор
    CPU = models.ForeignKey('SmartPhoneCPU', related_name='smartphones',
                            on_delete=models.PROTECT, verbose_name='Процессор')

    # Оперативная память
    RAM = models.PositiveSmallIntegerField(verbose_name='Оперативная память (RAM)')

    # Встроенная память
    ROM = models.PositiveSmallIntegerField(verbose_name='Встроенная память (ROM)')

    # Основная камера
    number_of_main_cameras = models.PositiveSmallIntegerField(verbose_name='Кол-во основных камер (шт)')
    optical_stabilization = models.BooleanField(default=False, verbose_name='Оптическая стабилизация')
    digital_stabilization = models.BooleanField(default=False, verbose_name='Цифровая стабилизация')
    LiDAR_scanner = models.BooleanField(default=False, verbose_name='Сканер LiDAR')
    video_resolution_horizontal = models.PositiveIntegerField(verbose_name='Разрешение видеосъемки по горизонтали')
    video_resolution_vertical = models.PositiveIntegerField(verbose_name='Разрешение видеосъемки по вертикали')

    # Фронтальная камера
    number_of_front_cameras = models.PositiveIntegerField(verbose_name='Кол-во фронтальных камер (шт)')

    # SIM карты
    SIM_card = models.ForeignKey('SIMCard', related_name='smartphones', on_delete=models.PROTECT)

    # Передача данных
    data_transmission_standards = models.ManyToManyField('DataTransmissionStandard', related_name='smartphones',
                                                         verbose_name='Поддержка стандартов')
    NFC = models.BooleanField(verbose_name='Технология NFC')
    bluetooth_module = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='Встроенный модуль Bluetooth')

    # Функции
    GPS = models.BooleanField(default=False, verbose_name='Поддержка GPS')
    glonass = models.BooleanField(default=False, verbose_name='Поддержка ГЛОНАСС')
    sensors = models.ManyToManyField('SmartPhoneSensor', related_name='smartphones', verbose_name='Датчики')

    # Безопасность
    face_recognition = models.BooleanField(default=False, verbose_name='Сенсор распознавания лица')
    fingerprint_scanner = models.BooleanField(default=False, verbose_name='Сканер отпечатка пальца')

    # Интерфейсы
    USB_port = models.ForeignKey('SmartPhoneUSBPort', related_name='smartphones',
                                 on_delete=models.PROTECT, verbose_name='Порт USB')

    # Корпус
    body_materials = models.ManyToManyField('SmartPhoneBodyMaterial', related_name='smartphones',
                                            verbose_name='Материал корпуса')
    protection_degree = models.ForeignKey('SmartPhoneBodyProtection', related_name='smartphones',
                                          on_delete=models.PROTECT, blank=True, null=True,
                                          verbose_name='Степень защиты')
    color = models.ForeignKey('SmartPhoneColor', related_name='smartphones', on_delete=models.PROTECT,
                              verbose_name='Цвет')

    # Электропитание
    charger_power = models.PositiveSmallIntegerField(verbose_name='Мощность блока питания (Вт)')
    battery_type = models.ForeignKey('SmartPhoneBatteryType', related_name='smartphones', on_delete=models.PROTECT,
                                     verbose_name='Тип аккумулятора')
    battery_capacity = models.PositiveSmallIntegerField(verbose_name='Емкость аккумулятора (мАч)')
    wireless_charging = models.BooleanField(default=False, verbose_name='Поддержка беспроводной зарядки')
    fast_charging = models.BooleanField(default=False, verbose_name='Поддержка быстрой зарядки')

    # Комплектация
    charger = models.BooleanField(default=False, verbose_name='Зарядное устройство')
    screen_protector = models.BooleanField(default=False, verbose_name='Защитная пленка для экрана')
    cable = models.ForeignKey('SmartPhoneCable', related_name='smartphones', on_delete=models.PROTECT,
                              verbose_name='Кабель')
    # Вес
    weight = models.PositiveSmallIntegerField(verbose_name='Вес (г)')

    # Габаритные размеры
    width = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Ширина (мм)')
    height = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Высота (мм)')
    depth = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Толщина (мм)')

    class Meta:
        ordering = ('brand', 'series', 'RAM', 'ROM', 'color')
        verbose_name = 'Смартфон'
        verbose_name_plural = 'Смартфоны'

    def __str__(self):
        title = f'Смартфон {self.brand} {self.series} {self.RAM}/{self.ROM}GB {self.color}'
        if self.model:
            title += f' ({self.model})'
        return title


class ManufacturerCountry(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')

    class Meta:
        verbose_name = 'Страна производитель'
        verbose_name_plural = 'Страны производители'

    def __str__(self):
        return self.title


class OperatingSystem(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название')

    class Meta:
        verbose_name = 'Операционная система'
        verbose_name_plural = 'Операционные системы'

    def __str__(self):
        return self.title


class SmartPhoneCPU(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    cores = models.PositiveSmallIntegerField(blank=True, verbose_name='Кол-во ядер')

    class Meta:
        verbose_name = 'Процессор смартфона'
        verbose_name_plural = 'Процессоры смартфонов'

    def __str__(self):
        return self.title


class SmartPhoneUSBPort(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название')

    class Meta:
        verbose_name = 'USB порт смартфона'
        verbose_name_plural = 'USB порты смартфонов'

    def __str__(self):
        return self.title


class ScreenTechnology(models.Model):
    title = models.CharField(max_length=6, verbose_name='Название')

    class Meta:
        verbose_name = 'Технология экрана'
        verbose_name_plural = 'Технологии экранов'

    def __str__(self):
        return self.title


class ScreenRefreshRate(models.Model):
    value = models.PositiveSmallIntegerField(verbose_name='Значение')

    class Meta:
        verbose_name = 'Частота обновления экрана'
        verbose_name_plural = 'Частоты обновления экрана'


class SmartPhoneMainCamera(models.Model):
    smartphone = models.ForeignKey(Smartphone, related_name='main_cameras', on_delete=models.CASCADE,
                                   verbose_name='Смартфон')
    megapixels = models.PositiveSmallIntegerField(verbose_name='МПикс')

    class Meta:
        verbose_name = 'Основная камера смартфона'
        verbose_name_plural = 'Основные камеры смартфона'

    def __str__(self):
        return f'{self.megapixels} МПикс'


class SmartPhoneFrontCamera(models.Model):
    smartphone = models.ForeignKey(Smartphone, related_name='front_cameras', on_delete=models.CASCADE,
                                   verbose_name='Смартфон')
    megapixels = models.PositiveSmallIntegerField(verbose_name='МПикс')

    class Meta:
        verbose_name = 'Фронтальная камера смартфона'
        verbose_name_plural = 'Фронтальные камеры смартфона'

    def __str__(self):
        return f'{self.megapixels} МПикс'


class SIMCard(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название')

    class Meta:
        verbose_name = 'SIM карта смартфона'
        verbose_name_plural = 'SIM карты смартфонов'

    def __str__(self):
        return self.title


class DataTransmissionStandard(models.Model):
    title = models.CharField(max_length=3, verbose_name='Название')

    class Meta:
        verbose_name = 'Стандарт передачи данных'
        verbose_name_plural = 'Стандарты передачи данных'

    def __str__(self):
        return self.title


class SmartPhoneSensor(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')

    class Meta:
        verbose_name = 'Датчик смартфона'
        verbose_name_plural = 'Датчики смартфонов'

    def __str__(self):
        return self.title


class SmartPhoneBodyMaterial(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')

    class Meta:
        verbose_name = 'Материал корпуса смартфона'
        verbose_name_plural = 'Материалы корпусов смартфонов'

    def __str__(self):
        return self.title


class SmartPhoneBodyProtection(models.Model):
    title = models.CharField(max_length=10, verbose_name='Название')

    class Meta:
        verbose_name = 'Степень защиты корпуса смартфона'
        verbose_name_plural = 'Степень защиты корпуса смартфона'

    def __str__(self):
        return self.title


class SmartPhoneColor(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название')

    class Meta:
        verbose_name = 'Цвет смартфона'
        verbose_name_plural = 'Цвета смартфонов'

    def __str__(self):
        return self.title


class SmartPhoneCable(models.Model):
    to_phone = models.CharField(max_length=15, verbose_name='Штекер в смартфон')
    to_charger = models.CharField(max_length=15, verbose_name='Штекер в зарядное устройство')

    class Meta:
        verbose_name = 'Кабель смартфона'
        verbose_name_plural = 'Кабель смартфона'

    def __str__(self):
        return f'{self.to_phone} - {self.to_charger}'


class SmartPhoneBatteryType(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')

    class Meta:
        verbose_name = 'Тип батареи смартфона'
        verbose_name_plural = 'Типы батарей смартфонов'

    def __str__(self):
        return self.title
