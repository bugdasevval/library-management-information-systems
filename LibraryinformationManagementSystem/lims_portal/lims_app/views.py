from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import reader
from .models import *
from .models import Record
from django.shortcuts import render, redirect, get_object_or_404
from .models import LoanDetail, reader, Record

def home(request):
    return render(request, "home.html", context={"current_tab": "home"})

def readers(request):
    readers = reader.objects.all()
    return render(request, "readers.html", context={"current_tab": "readers", "readers": readers})

def books(request):
    books = Bookso.objects.all()
    return render(request, "books.html", context={"current_tab": "books", "books": books})

def returns(request):
    return render(request, "returns.html", context={"current_tab": "returns"})

def save_student(request):
    if request.method == 'POST':
        reference_name = request.POST.get('reference_name')
        reference_contact = request.POST.get('reference_contact')
        reference_id = request.POST.get('reference_id')
        reader_address = request.POST.get('reader_address')

        new_reader = reader(reference_name=reference_name, reference_contact=reference_contact, reference_id=reference_id, reader_address=reader_address)
        new_reader.save()

        readers = reader.objects.all()
        return render(request, 'readers.html', {'current_tab': 'readers', 'readers': readers})

    return render(request, 'readers.html', {'current_tab': 'readers'})

def readers_tab(request):
    readers = reader.objects.all()
    return render(request, "readers.html", context={"current_tab": "readers", "readers": readers})

def save_loan(request):
    if request.method == 'POST':
        tc = request.POST.get('tc')
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        book = request.POST.get('book')
        date = request.POST.get('date')

        new_loan = LoanDetail(tc=tc, name=name, surname=surname, book=book, date=date)
        new_loan.save()

        return redirect('kayit')

    return render(request, 'returns.html')

def kayit(request):
    query = request.GET.get('query')
    if query:
        loans = LoanDetail.objects.filter(tc__icontains=query)
    else:
        loans = LoanDetail.objects.all()
    return render(request, 'kayit.html', {'loans': loans})

def delete_loan(request, id):
    loan = get_object_or_404(LoanDetail, id=id)
    loan.delete()
    return redirect('kayit')

def edit_loan(request, id):
    loan = get_object_or_404(LoanDetail, id=id)
    if request.method == 'POST':
        loan.tc = request.POST.get('tc')
        loan.name = request.POST.get('name')
        loan.surname = request.POST.get('surname')
        loan.book = request.POST.get('book')
        loan.date = request.POST.get('date')
        loan.save()
        return redirect('kayit')
    return render(request, 'edit_loan.html', {'loan': loan})


def ceza_view(request):
    if 'search_id' in request.GET:
        search_id = request.GET['search_id']
        records = Record.objects.filter(id=search_id)
    else:
        records = Record.objects.all()

    context = {
        'records': records
    }
    return render(request, 'ceza.html', context)

def search_reader(request):
    query = request.GET.get('query')
    if query:
        readers = reader.objects.filter(reference_id__icontains=query)
    else:
        readers = reader.objects.all()
    return render(request, 'readers.html', {'current_tab': 'readers', 'readers': readers})

def edit_reader(request, id):
    selected_reader = get_object_or_404(reader, pk=id)
    if request.method == 'POST':
        selected_reader.reference_name = request.POST.get('reference_name')
        selected_reader.reference_contact = request.POST.get('reference_contact')
        selected_reader.reader_address = request.POST.get('reader_address')
        selected_reader.save()
        return redirect('readers_tab')
    return render(request, 'edit_reader.html', {'reader': selected_reader})

def delete_reader(request, id):
    selected_reader = get_object_or_404(reader, pk=id)
    selected_reader.delete()
    return redirect('readers_tab')



