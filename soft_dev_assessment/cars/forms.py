from django import forms  
from cars.models import Car 

class CarForm(forms.ModelForm):  
    class Meta:  
        model = Car  
        exclude = ('position',)