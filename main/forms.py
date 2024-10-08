from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "rating", "stock"]    
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'border border-pink-300 rounded-lg p-2'
            })
    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)
    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)