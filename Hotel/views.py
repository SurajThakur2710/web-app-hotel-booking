from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import hotel


def welcome(request):
    return HttpResponse("<h1> Welcome User! <h1/>")

def hotelviews(request):
    allhotel = hotel.objects.filter(status=hotel.APPROVED)
    return render(request, 'MAIN.html', {'hoteldata':allhotel})

def aboutus(request):
    return render(request, 'about us/about us page.html')

def contactus(request):
    return render(request, 'contact us/contact us.html')

def Hotels(request):
    allhotel = hotel.objects.filter(status=hotel.APPROVED)
    return render(request, 'HotelList/HotelList.html',{'hoteldata':allhotel})





