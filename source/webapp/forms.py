from django import forms
from .models import STATUS_CHOICES

default_status = STATUS_CHOICES[0][0]


BROWSER_DATETIME_FORMAT = '%Y-%m-%dT%H:%M'


class RecordForm(forms.Form):
    author = forms.CharField(max_length=200, required=True, label='Автор')
    text = forms.CharField(max_length=3000, required=True, label="Текст",
                           widget=forms.Textarea)
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True, label='Статус',
                               initial=default_status)
    email = forms.EmailField(required=True, label='Почта')