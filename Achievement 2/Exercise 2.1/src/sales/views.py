from django.shortcuts import render
# to protect function based views
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    # Renders home.html file
    return render(request, 'sales/home.html')

# Define function based view
@login_required
def records(request):
    # Simply display page
    return render(request, 'sales/records.html')