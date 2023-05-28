from django.contrib import admin
from .models import Category, medicineItem


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'vendor', 'updated_at')
    search_fields = ('category_name', 'vendor__vendor_name')


class medicineItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('medicine_title',)}
    list_display = ('medicine_title', 'category', 'vendor', 'price', 'is_available', 'updated_at')
    search_fields = ('medicine_title', 'category__category_name', 'vendor__vendor_name', 'price')
    list_filter = ('is_available',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(medicineItem, medicineItemAdmin)
