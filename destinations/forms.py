from django import forms
from django.forms import ModelForm
from .models import Destinations, Galary, Messages





class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destinations
        exclude= ['Created_date']

class GalaryForm(forms.ModelForm):
    class Meta:
        model = Galary
        exclude = ['title']


class EditDestinationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(), max_length=50, required=False)
    picture = forms.ImageField(required=False)
    description = forms.CharField(widget=forms.TextInput(), max_length=200, required=False)

    class Meta:
        model = Destinations
        fields = ('name', 'picture', 'description')



class MesgeForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ('name','mail','number','mesge')