from django.shortcuts import render
from .models import Packages, Places


def home(request):
    packages = []
    if request.method == "POST":
        for package in Packages.objects.all():
            data = str(request.POST['search'])
            if package.places.filter(place_name=data.lower()).exists():
                packages.append(package)
    return render(request, 'home.html', {
        'packages': packages
    })

def deals(request):
    return render(request, 'deals.html', {
        'deals': Places.objects.all()
    })

def about(request):
    return render(request, 'about.html', {})

def reservation(request):
    return render(request, 'reservation.html', {})