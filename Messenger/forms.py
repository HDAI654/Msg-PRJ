from django import forms

class fmessage(forms.Form):
    def __init__(self, *args, **kwargs):
        super(fmessage, self).__init__(*args, **kwargs)
        for item in self.visible_fields():
            item.field.widget.attrs['class'] = 'form-control w-100 bg-light'
    text = forms.CharField(max_length=5000, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter your message'}))