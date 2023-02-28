from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.

 
def members(request):
    return render(request, 'members/index.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi, {username}, your account was created successfully' )
            return redirect("members")
    else:
        form = UserRegisterForm()

    return render(request, 'members/register.html', {'form':form})



def compound_interest(request):
    if request.method == 'POST':
        principal = float(request.POST['principal'])
        rate = float(request.POST['rate']) / 100
        years = int(request.POST['years'])
        monthly_contrib = float(request.POST['monthly_contrib'])
        months = years * 12
        amount = principal
        for i in range(months):
            amount += monthly_contrib
            amount *= (1 + rate/12)
        result = f"${amount:.2f}"
    else:
        result = None
    return render(request, 'members/compound_interest.html', {'result': result})


def simple_int(request):
    if request.method == 'POST':
        years = int(request.post["num"])
        rate = int (request.post["rate"])
        intial_inv = int(request.post["initial_inv"])
        simple_interest = rate/100*(intial_inv)*years
    else:
        simple_interest = None
    return render(request, "members/simple.html", {"simple_interest": simple_interest})



@login_required

def profile(request):
    user = request.user
    context = {'user': user}
    return render(request, 'members/profile.html', context)

from django.shortcuts import render



