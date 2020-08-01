from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import RecordForm
from webapp.models import Record


def index_view(request):
    data = Record.objects.filter(status='active')
    return render(request, 'index.html', context={
        'records': data
    })


def record_create_view(request):
    if request.method == "GET":
        form = RecordForm()
        return render(request, 'record_create.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = RecordForm(data=request.POST)
        if form.is_valid():
            record = Record.objects.create(
                author=form.cleaned_data['author'],
                text=form.cleaned_data['text'],
                email=form.cleaned_data['email'],
                status=form.cleaned_data['status']
            )
            return redirect('index')
        else:
            return render(request, 'record_create.html', context={
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def record_update_view(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == "GET":
        form = RecordForm(initial={
            'author': record.author,
            'text': record.text,
            'email': record.email,
            'status': record.status,
        })
        return render(request, 'record_update.html', context={
            'form': form,
            'record': record
        })
    elif request.method == 'POST':
        form = RecordForm(data=request.POST)
        if form.is_valid():
            record.author = form.cleaned_data['author']
            record.text = form.cleaned_data['text']
            record.email = form.cleaned_data['email']
            record.status = form.cleaned_data['status']
            record.save()
            return redirect('index')
        else:
            return render(request, 'record_update.html', context={
                'record': record,
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def record_delete_view(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == 'GET':
        return render(request, 'record_delete.html', context={'record': record})
    elif request.method == 'POST':
        record.delete()
        return redirect('index')
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])