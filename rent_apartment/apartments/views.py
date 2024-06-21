from django.shortcuts import render, redirect
from .models import Apartment
from .forms import ApartmentForm

def apartment_list(request):
    apartments = Apartment.objects.all()
    return render(request, 'apartments/apartment_list.html', {'apartments': apartments})

def apartment_create(request):
    if request.method == 'POST':
        form = ApartmentForm(request.POST)
        if form.is_valid():
            apartment = form.save(commit=False)
            apartment.owner = request.user
            apartment.save()
            return redirect('apartment_list')
    else:
        form = ApartmentForm()
    return render(request, 'apartments/apartment_form.html', {'form': form})
