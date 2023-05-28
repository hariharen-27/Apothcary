from django.contrib import admin
from .models import Payment, Order, Orderedmedicine


class OrderedmedicineInline(admin.TabularInline):
    model = Orderedmedicine
    readonly_fields = ('order', 'payment', 'user', 'medicineitem', 'quantity', 'price', 'amount')
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'name', 'phone', 'email', 'total', 'payment_method', 'status', 'order_placed_to', 'is_ordered']
    inlines = [OrderedmedicineInline]


admin.site.register(Payment)
admin.site.register(Order, OrderAdmin)
admin.site.register(Orderedmedicine)
