from django import forms
from .models import ReadingRecord
import datetime

class RecordForm(forms.ModelForm):
    class Meta:
        model = ReadingRecord
        fields = ['title', 'author', 'rep_img', 'record_title', 'read_at', 'category', 'record_body']
    
    read_at = forms.DateField(initial=datetime.date.today,widget=forms.DateInput(attrs={'required': 'required', }))
