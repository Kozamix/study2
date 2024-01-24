from django.shortcuts import render, redirect, get_object_or_404
from .models import Car
from .forms import CarForm

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})
def edit_car(request, pk):
    car = get_object_or_404(Car, id=pk)

    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm(instance=car)

    # Отримання параметра 'delete' з GET-запиту
    delete_request = request.GET.get('delete', None)
    if delete_request:
        car.delete()
        return redirect('car_list')

    return render(request, 'cars/edit_car.html', {'form': form, 'car': car})


def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('car_list')
        else:
            return render(request, 'cars/add_car.html', {'form': form})
    else:
        form = CarForm()

    return render(request, 'cars/add_car.html', {'form': form})

def edit_car_view(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'cars/car_detail.html', {'car': car})
def delete_car(request, pk):
    car = get_object_or_404(Car, id=pk)
    car.delete()
    return redirect('car_list')
