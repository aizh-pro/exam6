from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect

from webapp.forms import RecordForm
from webapp.models import Record


def index_view(request):
    data = Record.objects.filter(status='active')
    return render(request, 'index.html', context={
        'records': data
    })


def record_create_view(request):
    if request.method == 'GET':
        form = RecordForm()
        return render(request, 'record_create.html', context={
            'form': form})
    elif request.method == 'POST':
        form = RecordForm(data=request.POST)
        if form.is_valid():
            # record = Record.objects.create(**form.cleaned_data)
            return redirect('index')
        else:
            return render(request, 'record_create.html', context={
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])