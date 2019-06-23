from django import forms
    

class LocationForm(forms.Form):
    county = forms.CharField(label='County Name', max_length=50)
    code = forms.IntegerField(label='County Code')