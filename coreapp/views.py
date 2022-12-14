from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return redirect(restaurant_home)

@login_required(login_url='/restaurant/sign_in/')
def restaurant_home(request):
    return render(request, 'restaurant/home.html', {})