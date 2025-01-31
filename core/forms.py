from django import forms
from .models import Lessons, Contact

class LessonsForm(forms.ModelForm):
    class Meta:
        model = Lessons
        fields = ['title', 'description', 'tutorial'] 

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter lesson title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter lesson description'}),
            'tutorial': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        return title.strip()


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your Email'}))
    subject = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message', 'rows': 5}))