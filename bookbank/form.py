from django import forms
from .models import ReadingRecord

class RecordForm(forms.ModelForm):
    class Meta:
        model = ReadingRecord
        fields = ['title', 'author', 'record_title', 'read_at', 'category', 'record_body']