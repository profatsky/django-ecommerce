# Generated by Django 4.1.7 on 2023-04-02 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BatteryType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип аккумулятора гаджета',
                'verbose_name_plural': 'Тип аккумулятора гаджета',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Название')),
                ('slug', models.SlugField(max_length=80, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренды',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Название')),
                ('slug', models.SlugField(max_length=80, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='DataTransmissionStandard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Стандарт передачи данных',
                'verbose_name_plural': 'Стандарты передачи данных',
            },
        ),
        migrations.CreateModel(
            name='GadgetBodyMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Материал корпуса',
                'verbose_name_plural': 'Материалы корпуса',
            },
        ),
        migrations.CreateModel(
            name='GadgetCable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_gadget', models.CharField(max_length=15, verbose_name='Штекер в гаджет')),
                ('to_charger', models.CharField(max_length=15, verbose_name='Штекер в зарядное устройство')),
            ],
            options={
                'verbose_name': 'Кабель для гаджета',
                'verbose_name_plural': 'Кабель для гаджета',
            },
        ),
        migrations.CreateModel(
            name='GadgetColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Цвет гаджета',
                'verbose_name_plural': 'Цвета гаджета',
            },
        ),
        migrations.CreateModel(
            name='HeadphonesConnectionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип подключения наушников',
                'verbose_name_plural': 'Тип подключения наушников',
            },
        ),
        migrations.CreateModel(
            name='HeadphonesType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип наушников',
                'verbose_name_plural': 'Тип наушников',
            },
        ),
        migrations.CreateModel(
            name='ManufacturerCountry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Страна производитель',
                'verbose_name_plural': 'Страны производители',
            },
        ),
        migrations.CreateModel(
            name='OperatingSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Операционная система',
                'verbose_name_plural': 'Операционные системы',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True, verbose_name='URL')),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d', verbose_name='Изображение')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена со скидкой')),
                ('units', models.PositiveIntegerField(default=0, verbose_name='Кол-во')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.brand', verbose_name='Бренд')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='shop.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='ScreenTechnology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Технология экрана',
                'verbose_name_plural': 'Технологии экранов',
            },
        ),
        migrations.CreateModel(
            name='SIMCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'SIM карта',
                'verbose_name_plural': 'SIM карты',
            },
        ),
        migrations.CreateModel(
            name='SmartPhoneBodyProtection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Степень защиты корпуса',
                'verbose_name_plural': 'Степень защиты корпуса',
            },
        ),
        migrations.CreateModel(
            name='SmartPhoneCPU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('cores', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Кол-во ядер')),
            ],
            options={
                'verbose_name': 'Процессор смартфона',
                'verbose_name_plural': 'Процессоры смартфонов',
            },
        ),
        migrations.CreateModel(
            name='SmartPhoneSensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Датчик смартфона',
                'verbose_name_plural': 'Датчики смартфонов',
            },
        ),
        migrations.CreateModel(
            name='SmartPhoneUSBPort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'USB порт смартфона',
                'verbose_name_plural': 'USB порты смартфонов',
            },
        ),
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.product')),
                ('guarantee', models.PositiveSmallIntegerField(blank=True, verbose_name='Гарантия')),
                ('series', models.CharField(blank=True, max_length=30, verbose_name='Серия')),
                ('model', models.CharField(blank=True, max_length=30, verbose_name='Модель')),
                ('screen_diagonal', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Диагональ экрана в дюймах')),
                ('screen_resolution_vertical', models.PositiveSmallIntegerField(verbose_name='Разрешение экрана по вертикали')),
                ('screen_resolution_horizontal', models.PositiveSmallIntegerField(verbose_name='Разрешение экрана по горизонтали')),
                ('screen_refresh_rate', models.PositiveSmallIntegerField(default=60, verbose_name='Частота обновления экрана (Гц)')),
                ('RAM', models.PositiveSmallIntegerField(verbose_name='Оперативная память (RAM)')),
                ('ROM', models.PositiveSmallIntegerField(verbose_name='Встроенная память (ROM)')),
                ('number_of_main_cameras', models.PositiveSmallIntegerField(verbose_name='Кол-во основных камер (шт)')),
                ('optical_stabilization', models.BooleanField(default=False, verbose_name='Оптическая стабилизация')),
                ('digital_stabilization', models.BooleanField(default=False, verbose_name='Цифровая стабилизация')),
                ('LiDAR_scanner', models.BooleanField(default=False, verbose_name='Сканер LiDAR')),
                ('video_resolution_horizontal', models.PositiveIntegerField(verbose_name='Разрешение видеосъемки по горизонтали')),
                ('video_resolution_vertical', models.PositiveIntegerField(verbose_name='Разрешение видеосъемки по вертикали')),
                ('number_of_front_cameras', models.PositiveIntegerField(verbose_name='Кол-во фронтальных камер (шт)')),
                ('NFC', models.BooleanField(verbose_name='Технология NFC')),
                ('bluetooth_module', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Встроенный модуль Bluetooth')),
                ('GPS', models.BooleanField(default=False, verbose_name='Поддержка GPS')),
                ('glonass', models.BooleanField(default=False, verbose_name='Поддержка ГЛОНАСС')),
                ('face_recognition', models.BooleanField(default=False, verbose_name='Сенсор распознавания лица')),
                ('fingerprint_scanner', models.BooleanField(default=False, verbose_name='Сканер отпечатка пальца')),
                ('charger_power', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Мощность блока питания (Вт)')),
                ('battery_capacity', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Емкость аккумулятора (мАч)')),
                ('wireless_charging', models.BooleanField(default=False, verbose_name='Поддержка беспроводной зарядки')),
                ('fast_charging', models.BooleanField(default=False, verbose_name='Поддержка быстрой зарядки')),
                ('charger', models.BooleanField(default=False, verbose_name='Зарядное устройство')),
                ('screen_protector', models.BooleanField(default=False, verbose_name='Защитная пленка для экрана')),
                ('weight', models.PositiveSmallIntegerField(verbose_name='Вес (г)')),
                ('width', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Ширина (мм)')),
                ('height', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Высота (мм)')),
                ('depth', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Толщина (мм)')),
                ('CPU', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='smartphones', to='shop.smartphonecpu', verbose_name='Процессор')),
                ('SIM_card', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='smartphones', to='shop.simcard')),
                ('USB_port', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='smartphones', to='shop.smartphoneusbport', verbose_name='Порт USB')),
                ('battery_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='smartphones', to='shop.batterytype', verbose_name='Тип аккумулятора')),
                ('body_materials', models.ManyToManyField(related_name='smartphones', to='shop.gadgetbodymaterial', verbose_name='Материал корпуса')),
                ('cable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='smartphones', to='shop.gadgetcable', verbose_name='Кабель')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='smartphones', to='shop.gadgetcolor', verbose_name='Цвет')),
                ('data_transmission_standards', models.ManyToManyField(related_name='smartphones', to='shop.datatransmissionstandard', verbose_name='Поддержка стандартов')),
                ('manufacturer_country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='smartphones', to='shop.manufacturercountry', verbose_name='Страна производитель')),
                ('operating_system', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='smartphones', to='shop.operatingsystem', verbose_name='Операционная система')),
                ('protection_degree', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='smartphones', to='shop.smartphonebodyprotection', verbose_name='Степень защиты')),
                ('screen_technology', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='smartphones', to='shop.screentechnology', verbose_name='Технология экрана')),
                ('sensors', models.ManyToManyField(related_name='smartphones', to='shop.smartphonesensor', verbose_name='Датчики')),
            ],
            options={
                'verbose_name': 'Смартфон',
                'verbose_name_plural': 'Смартфоны',
                'ordering': ('brand', 'series', 'RAM', 'ROM', 'color'),
            },
            bases=('shop.product',),
        ),
        migrations.CreateModel(
            name='SmartPhoneMainCamera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('megapixels', models.PositiveSmallIntegerField(verbose_name='МПикс')),
                ('smartphone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_cameras', to='shop.smartphone', verbose_name='Смартфон')),
            ],
            options={
                'verbose_name': 'Основная камера смартфона',
                'verbose_name_plural': 'Основные камеры смартфона',
            },
        ),
        migrations.CreateModel(
            name='SmartPhoneFrontCamera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('megapixels', models.PositiveSmallIntegerField(verbose_name='МПикс')),
                ('smartphone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='front_cameras', to='shop.smartphone', verbose_name='Смартфон')),
            ],
            options={
                'verbose_name': 'Фронтальная камера смартфона',
                'verbose_name_plural': 'Фронтальные камеры смартфона',
            },
        ),
        migrations.CreateModel(
            name='Headphones',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.product')),
                ('guarantee', models.PositiveSmallIntegerField(blank=True, verbose_name='Гарантия')),
                ('series', models.CharField(blank=True, max_length=30, verbose_name='Серия')),
                ('model', models.CharField(blank=True, max_length=30, verbose_name='Модель')),
                ('bluetooth_version', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Версия Bluetooth')),
                ('built_in_microphone', models.BooleanField(default=True, verbose_name='Встроенный микрофон')),
                ('active_noise_control', models.BooleanField(default=False, verbose_name='Система активного подавления шума')),
                ('use_as_headset', models.BooleanField(default=True, verbose_name='Использование в качестве гарнитуры')),
                ('playback_control', models.BooleanField(default=True, verbose_name='Управление воспроизведением')),
                ('fast_charging', models.BooleanField(default=False, verbose_name='Быстрая зарядка')),
                ('wireless_charging', models.BooleanField(default=False, verbose_name='Беспроводная зарядка')),
                ('battery_capacity', models.PositiveSmallIntegerField(null=True, verbose_name='Емкость аккумулятора (мАч)')),
                ('charging_from_USB_port', models.BooleanField(default=True, verbose_name='Зарядка от USB порта')),
                ('splashproof_body', models.BooleanField(default=False, verbose_name='Брызгозащитный корпус')),
                ('charger', models.BooleanField(default=False, verbose_name='Зарядное устройство')),
                ('ear_pads_pairs', models.PositiveSmallIntegerField(default=0, verbose_name='Пар амбушюров в комплекте')),
                ('weight', models.PositiveSmallIntegerField(verbose_name='Вес (г)')),
                ('battery_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='headphones', to='shop.batterytype', verbose_name='Тип аккумулятора')),
                ('body_materials', models.ManyToManyField(related_name='headphones', to='shop.gadgetbodymaterial', verbose_name='Материал корпуса')),
                ('cable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='headphones', to='shop.gadgetcable', verbose_name='Кабель')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='headphones', to='shop.gadgetcolor', verbose_name='Цвет')),
                ('connection_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='headphones', to='shop.headphonesconnectiontype', verbose_name='Тип подключения наушников')),
                ('manufacturer_country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='headphones', to='shop.manufacturercountry', verbose_name='Страна производитель')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='headphones', to='shop.headphonestype', verbose_name='Тип наушников')),
            ],
            options={
                'verbose_name': 'Наушники',
                'verbose_name_plural': 'Наушники',
            },
            bases=('shop.product',),
        ),
    ]
