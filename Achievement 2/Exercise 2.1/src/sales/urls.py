from django.urls import path
from . import views
from .views import home, records

app_name = 'sales'

urlpatterns = [
    path('', views.home, name='home'),  # Maps the home view to the '' URL (i.e., /sales/)
    path('sales/', records, name='records')
]
