from django import forms

class FilterForm(forms.Form):
    year = forms.IntegerField(required=False, label='Filter by Year', widget=forms.NumberInput(attrs={'min': 1980, 'max': 2030}))
    month = forms.IntegerField(required=False, label='Filter by Month', widget=forms.NumberInput(attrs={'min': 1, 'max': 12}))
