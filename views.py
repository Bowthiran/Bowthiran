from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):
    # dest1 = Destination()
    # dest1.name = "Bali"
    # dest1.desc = "City That Never Sleeps"
    # dest1.img = "destination_1.jpg"
    # dest1.price = 800
    # dest1.offer = True

    # dest2 = Destination()
    # dest2.name = "Hyderabad"
    # dest2.desc = "First Biriyani Then Sherwani"
    # dest2.img = "destination_6.jpg"
    # dest2.price = 750

    # dest3 = Destination()
    # dest3.name = "Bangalore"
    # dest3.desc = "Land of Sandalwoods"
    # dest3.img = "destination_3.jpg"
    # dest3.price = 700

    # dest4 = Destination()
    # dest4.name = "Mumbai"
    # dest4.desc = "The Massive Gateway"
    # dest4.img = "destination_4.jpg"
    # dest4.price = 700

    # dest5 = Destination()
    # dest5.name = "Phi Phi Island"
    # dest5.desc = "Most Beautiful Mountain World"
    # dest5.img = "destination_5.jpg"
    # dest5.price = 800
    # dest5.offer = True

    # dest6 = Destination()
    # dest6.name = "Indonesia"
    # dest6.desc = "The Economy in Southeast Asia"
    # dest6.img = "destination_2.jpg"
    # dest6.price = 750
    
    # dests = [dest1, dest2, dest3, dest4, dest5, dest6]

    dests = Destination.objects.all()

    return render(request,"index.html",{'dests':dests})