from django.forms import ModelForm, TextInput
from .models import City
from django.forms import ModelForm


class CityForm(ModelForm):
    class Meta:
        model = City
        fields =['name']
        # this is updated to have place holders
        widgets = {  
            'name': TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'}),
        }