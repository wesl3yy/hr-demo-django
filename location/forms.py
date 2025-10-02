from django import forms

class LocationSearchForm(forms.Form):
    keyword = forms.CharField(max_length=200, required=True)
    page = forms.IntegerField(min_value=1, required=False, initial=1)
    page_size = forms.IntegerField(min_value=1, max_value=100, required=False, initial=10)
