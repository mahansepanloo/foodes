from django import forms


class add(forms.Form):
    num = forms.IntegerField(max_value=10,min_value=0)

class off(forms.Form):
    off = forms.CharField()


