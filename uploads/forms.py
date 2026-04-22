from django import forms
from .models import UploadedFile

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']

    def clean_file(self):
        file = self.cleaned_data['file']
        ext = file.name.split('.')[-1].lower()
        if ext not in ['csv', 'xlsx', 'xls']:
            raise forms.ValidationError('Only CSV and Excel files are allowed.')
        return file
