from django.shortcuts import render, get_object_or_404, redirect
from.models import Apartment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from.forms import ApartmentForm

@login_required
def apartment_create(request):
    if request.method == 'POST':
        form = ApartmentForm(request.POST)
        if form.is_valid():
            apartment = form.save(commit=False)
            apartment.owner = request.user
            apartment.save()
            return redirect('index')
    else:
        form = ApartmentForm()
    return render(request, 'apartment_form.html', {'form': form})

@login_required
def apartment_edit(request, id):
    apartment = get_object_or_404(Apartment, id=id)
    if request.method == 'POST':
        form = ApartmentForm(request.POST, instance=apartment)
        if form.is_valid():
            form.save()
            return redirect('apartment_detail', id=apartment.id)
    else:
        form = ApartmentForm(instance=apartment)
    return render(request, 'apartment_form.html', {'form': form})

def index(request):
    apartments = Apartment.objects.all()
    return render(request, 'index.html', {'apartments': apartments})

def apartment_detail(request, id):
    apartment = get_object_or_404(Apartment, id=id)
    return render(request, 'apartment_detail.html', {'apartment': apartment})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
