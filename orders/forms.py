from django import forms


class add(forms.Form):
    num = forms.IntegerField(max_value=10,min_value=0)
class rateandcommentform(forms.Form):
    rate = forms.IntegerField(max_value=10,min_value=0)
    comment = forms.CharField(widget=(forms.Textarea()))

class off(forms.Form):
    off = forms.CharField()


class replycomment(forms.Form):
    replycomment = forms.CharField(widget=(forms.Textarea()))




