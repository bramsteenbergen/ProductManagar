from django import forms

class addProductForm(forms.Form):
    name = forms.CharField(max_length=30)
    alp_num_code = forms.CharField(max_length=30)
    stock = forms.IntegerField()
    description = forms.CharField(widget=forms.Textarea)
    id = forms.IntegerField(widget=forms.HiddenInput)