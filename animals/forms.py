from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'species', 'description', 'price', 'image', 'city']
        labels = {
            'name': 'Название',
            'species': 'Тип животного',
            'description': 'Дополнительное описание',
            'price': 'Цена',
            'image': 'Изображение',
            'city': 'Город',
        }

    image = forms.ImageField()
