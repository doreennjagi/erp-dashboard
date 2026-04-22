import pandas as pd
import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import FileUploadForm

@login_required
def upload_file(request):
    data = None
    columns = None
    error = None
    kpis = None
    chart_data = None

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

                if 'Type' in df.columns and 'Amount' in df.columns:
                    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce').fillna(0)
                    total_income = df[df['Type'] == 'Income']['Amount'].sum()
                    total_expenses = df[df['Type'] == 'Expense']['Amount'].sum()
                    balance = total_income - total_expenses

                    kpis = {
                        'total_income': f"{total_income:,.0f}",
                        'total_expenses': f"{total_expenses:,.0f}",
                        'balance': f"{balance:,.0f}",
                        'balance_positive': balance >= 0,
                    }

                    if 'Date' in df.columns:
                        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
                        df['Month'] = df['Date'].dt.strftime('%b %Y')
                        months = df['Month'].dropna().unique().tolist()

                        income_by_month = df[df['Type'] == 'Income'].groupby('Month')['Amount'].sum()
                        expense_by_month = df[df['Type'] == 'Expense'].groupby('Month')['Amount'].sum()

                        chart_data = json.dumps({
                            'labels': months,
                            'income': [float(income_by_month.get(m, 0)) for m in months],
                            'expenses': [float(expense_by_month.get(m, 0)) for m in months],
                        })

            except Exception as e:
                error = f"Could not read file: {str(e)}"
    else:
        form = FileUploadForm()

    return render(request, 'uploads/upload.html', {
        'form': form,
        'data': data,
        'columns': columns,
        'error': error,
        'kpis': kpis,
        'chart_data': chart_data,
    })
