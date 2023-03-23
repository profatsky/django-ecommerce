import csv
import datetime

from django.contrib import admin
from django.http import HttpResponse

from orders.models import OrderItem, Order


def export_to_csv(model_admin, request, queryset):
    options = model_admin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename=orders.csv'
    print(response['Content-Disposition'])
    writer = csv.writer(response)
    fields = list(filter(lambda x: not x.many_to_many and not x.one_to_many, options.get_fields()))
    writer.writerow([field.verbose_name for field in fields])
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ('product',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'address',
                    'postal_code', 'city', 'paid', 'created', 'updated')
    list_filter = ('paid', 'created', 'updated')
    readonly_fields = ('braintree_id',)
    inlines = [OrderItemInline]
    actions = [export_to_csv]


export_to_csv.short_description = 'Экспорт в CSV'
