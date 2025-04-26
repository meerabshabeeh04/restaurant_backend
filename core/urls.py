# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import MenuItemViewSet, ReservationViewSet

# router = DefaultRouter()
# router.register('menu', MenuItemViewSet)
# router.register('reservations', ReservationViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

from django.urls import path
from .views import MenuItemList, ReservationCreate

urlpatterns = [
    path('menu/', MenuItemList.as_view(), name='menu-list'),
    path('reserve/', ReservationCreate.as_view(), name='reservation-create'),
]
