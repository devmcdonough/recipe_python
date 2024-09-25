from django.shortcuts import render, redirect
# Django authentication libraries
from django.contrib.auth import authenticate, login, logout
# Django form for authentication
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    error_message = None
    form = AuthenticationForm()

    # When user hits login button then POST request is generated
    if request.method == 'POST':
    # Read data sent by the form via POST request
        form = AuthenticationForm(data=request.POST)
    # Check if form is valie
    if form.is_valid():
        # Read username
        username = form.cleaned_data.get('username')
        # Read password
        password = form.cleaned_data.get('password')
        # User Django authenticate to validate user
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('sales:records')
        else:
            error_message = 'Something went wrong'
        
    # prepare data to send from view to template
    context = {
        'form': form,
        'error_message': error_message
        }
    
    return render(request, 'auth/login.html', context)

# Defines function called logout_view that takes request from users
def logout_view(request):
    # Uses pre-defined Django function to logout
    logout(request)
    # After logging out goes back to login page
    return redirect('login')