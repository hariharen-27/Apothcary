from django import forms

from accounts.validators import allow_only_images_validator
from .models import Category, medicineItem


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'description']


class medicineItemForm(forms.ModelForm):
    image = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info w-100'}), validators=[allow_only_images_validator])
    class Meta:
        model = medicineItem
        fields = ['category', 'medicine_title', 'description', 'price', 'image', 'is_available']