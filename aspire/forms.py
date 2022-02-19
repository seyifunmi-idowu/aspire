from django import forms
from .models import Apply

class ApplyForm(forms.ModelForm):

    class Meta:
        model = Apply
        widgets = {
            'residential_address' : forms.Textarea(attrs={"rows":5, "cols":20}),
            'nok_address' : forms.Textarea(attrs={"rows":5, "cols":20}),
        }
        exclude = ()

