from django.shortcuts import render

# Create your views here.
def home(request):
    # Renders home.html file
    return render(request, 'sales/home.html')