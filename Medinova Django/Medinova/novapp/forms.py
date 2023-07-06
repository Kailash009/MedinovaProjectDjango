from novapp.models import Appoinment
from django import forms

class AppoinmentForms(forms.ModelForm):
    class Meta:
        model=Appoinment
        fields='__all__'

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for dpt in self.fields.values():
            dpt.widget.attrs['class']='form-control'
            
