import pandas as pd
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import FileUploadForm

@login_required
def upload_file(request):
    data = None
    columns = None
    error = None

    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded = form.save(commit=False)
            uploaded.user = request.user
            file = request.FILES['file']
            ext = file.name.split('.')[-1].lower()
            uploaded.file_name = file.name
            uploaded.file_type = 'csv' if ext == 'csv' else 'excel'
            uploaded.save()
            try:
                if ext == 'csv':
                    df = pd.read_csv(uploaded.file.path)
                else:
                    df = pd.read_excel(uploaded.file.path)
                columns = df.columns.tolist()
                data = df.head(50).values.tolist()
                uploaded.processed = True
                uploaded.save()
            except Exception as e:
                error = f"Could not read file: {str(e)}"
    else:
        form = FileUploadForm()

    return render(request, 'uploads/upload.html', {
        'form': form,
        'data': data,
        'columns': columns,
        'error': error,
    })
