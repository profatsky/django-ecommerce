from django.contrib import admin
from django.utils.text import slugify

from . import models
from .utils import translate


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)


class MainCameraInline(admin.StackedInline):
    model = models.SmartPhoneMainCamera


class FrontCameraInline(admin.StackedInline):
    model = models.SmartPhoneFrontCamera


@admin.register(models.Smartphone)
class SmartPhoneAdmin(admin.ModelAdmin):
    list_display = ('brand', 'series', 'model', 'RAM', 'ROM', 'color', 'price', 'discount_price', 'units')
    list_display_links = ('brand', 'series')
    list_filter = ('brand', 'color',)
    search_fields = ('category', 'brand', 'series', 'model')
    date_hierarchy = 'created'
    readonly_fields = ('slug', 'created', 'updated')
    raw_id_fields = ('category', 'brand', 'manufacturer_country', 'operating_system', 'screen_technology',
                     'CPU', 'SIM_card', 'USB_port', 'protection_degree', 'color', 'battery_type')
    fieldsets = (
        ('Информация о товаре', {'fields': ('category', 'brand', 'image', 'description',
                                            'price', 'discount_price', 'units', 'slug', 'created', 'updated')}),
        ('Заводские данные', {'fields': ('guarantee', 'manufacturer_country')}),
        ('Серия модель', {'fields': ('series', 'model')}),
        ('Операционная система', {'fields': ('operating_system',)}),
        ('Экран', {'fields': ('screen_diagonal', 'screen_resolution_vertical', 'screen_resolution_horizontal',
                              'screen_technology', 'screen_refresh_rate')}),
        ('Процессор', {'fields': ('CPU',)}),
        ('Оперативная память', {'fields': ('RAM',)}),
        ('Встроенная память', {'fields': ('ROM',)}),
        ('SIM карты', {'fields': ('SIM_card',)}),
        ('Передача данных', {'fields': ('data_transmission_standards', 'NFC', 'bluetooth_module')}),
        ('Функции', {'fields': ('GPS', 'glonass', 'sensors')}),
        ('Безопасность', {'fields': ('face_recognition', 'fingerprint_scanner')}),
        ('Интерфейсы', {'fields': ('USB_port',)}),
        ('Корпус', {'fields': ('body_materials', 'protection_degree', 'color')}),
        ('Электропитание', {'fields': ('charger_power', 'battery_type', 'battery_capacity', 'wireless_charging',
                                       'fast_charging')}),
        ('Комплектация', {'fields': ('charger', 'screen_protector', 'cable')}),
        ('Вес', {'fields': ('weight',)}),
        ('Габаритные размеры', {'fields': ('width', 'height', 'depth')}),
        ('Основная камера', {'fields': ('number_of_main_cameras', 'optical_stabilization', 'digital_stabilization',
                                        'LiDAR_scanner', 'video_resolution_horizontal', 'video_resolution_vertical')}),
        ('Фронтальная камера', {'fields': ('number_of_front_cameras',)}),
    )
    inlines = [MainCameraInline, FrontCameraInline]

    def save_model(self, request, obj, form, change):
        cd = form.cleaned_data
        obj.slug = "-".join((
            slugify(cd['brand']),
            slugify(cd['series']),
            slugify(cd['RAM']),
            slugify(cd['ROM']),
            slugify(translate(cd['color'].title))
        ))
        obj.save()


@admin.register(models.ManufacturerCountry)
class ManufacturerCountryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(models.OperatingSystem)
class OperatingSystemAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(models.SmartPhoneCPU)
class SmartPhoneCPUAdmin(admin.ModelAdmin):
    list_display = ('title', 'cores')


@admin.register(models.SmartPhoneUSBPort)
class SmartPhoneUSBPortAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(models.ScreenTechnology)
class ScreenTechnologyAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(models.SmartPhoneMainCamera)
class SmartPhoneMainCameraAdmin(admin.ModelAdmin):
    list_display = ('smartphone', 'megapixels')


@admin.register(models.SmartPhoneFrontCamera)
class SmartPhoneFrontCameraAdmin(admin.ModelAdmin):
    list_display = ('smartphone', 'megapixels')


@admin.register(models.SIMCard)
class SIMCardAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(models.DataTransmissionStandard)
class DataTransmissionStandardAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(models.SmartPhoneSensor)
class SmartPhoneSensorAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(models.GadgetBodyMaterial)
class GadgetBodyMaterialAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(models.SmartPhoneBodyProtection)
class SmartPhoneBodyProtectionAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(models.GadgetColor)
class GadgetColorAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(models.GadgetCable)
class GadgetCableAdmin(admin.ModelAdmin):
    list_display = ('to_gadget', 'to_charger')


@admin.register(models.BatteryType)
class BatteryTypeAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(models.Headphones)
class HeadphonesAdmin(admin.ModelAdmin):
    list_display = ('brand', 'type', 'series', 'model', 'color', 'price', 'discount_price', 'units')
    list_display_links = ('brand', 'series')
    list_filter = ('brand', 'color', 'type', 'connection_type')
    search_fields = ('category', 'brand', 'series', 'model')
    date_hierarchy = 'created'
    readonly_fields = ('slug', 'created', 'updated')
    raw_id_fields = ('category', 'brand', 'manufacturer_country', 'connection_type', 'type', 'battery_type',
                     'body_materials', 'cable', 'color')
    fieldsets = (
        ('Информация о товаре', {'fields': ('category', 'brand', 'image', 'description',
                                            'price', 'discount_price', 'units', 'slug', 'created', 'updated')}),
        ('Заводские данные', {'fields': ('guarantee', 'manufacturer_country')}),
        ('Серия модель', {'fields': ('series', 'model')}),
        ('Подключение', {'fields': ('connection_type',)}),
        ('Передача данных', {'fields': ('bluetooth_version',)}),
        ('Тип наушников', {'fields': ('type',)}),
        ('Микрофон', {'fields': ('built_in_microphone',)}),
        ('Функции', {'fields': ('active_noise_control', 'use_as_headset')}),
        ('Управление', {'fields': ('playback_control',)}),
        ('Зарядка', {'fields': ('fast_charging', 'wireless_charging')}),
        ('Электропитание', {'fields': ('battery_type', 'battery_capacity', 'charging_from_USB_port')}),
        ('Корпус', {'fields': ('body_materials', 'splashproof_body')}),
        ('Комплектация', {'fields': ('charger', 'cable', 'ear_pads_pairs')}),
        ('Цвет', {'fields': ('color',)}),
        ('Вес', {'fields': ('weight',)})
    )

    def save_model(self, request, obj, form, change):
        cd = form.cleaned_data
        obj.slug = "-".join((
            slugify(cd['brand']),
            slugify(cd['series']),
            slugify(cd['model']) if cd['model'] else '',
            slugify(translate(cd['color'].title))
        ))
        obj.save()


@admin.register(models.HeadphonesConnectionType)
class HeadphonesConnectionTypeAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(models.HeadphonesType)
class HeadphonesTypeAdmin(admin.ModelAdmin):
    list_display = ('title',)
