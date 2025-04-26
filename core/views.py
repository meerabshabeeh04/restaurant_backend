from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import MenuItem, Reservation
from .serializers import MenuItemSerializer, ReservationSerializer

class MenuItemList(generics.ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class ReservationCreate(generics.CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

