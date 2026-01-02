from django.urls import path,include
from .views import RegisterView,LoginView,BusListCreateView,BusDetailView,UserBookingView,BookingView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'BusDetails',BusDetailView)

urlpatterns = [
    path('buses/',BusListCreateView.as_view(), name='buses'),
    path('auth/signup/',RegisterView.as_view(),name='signup'),
    path('auth/login/',LoginView.as_view(), name='login'),
    path('user-bookings/<int:user_id>/',UserBookingView.as_view(), name='user-bookings'),
    path('bookings/', BookingView.as_view(), name='bookings'),
    path('',include(router.urls)),
    
]
