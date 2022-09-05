from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views import View
from django.urls import reverse
from django.http import JsonResponse

import stripe

stripe.api_key = "sk_test_51LdvOzEaorUnBrhGEBQwSIsKCYNZSdIWxMiP5A4RUnaFG5GgMvNCldpbmqHh7cwbpPNZyQpJShcVGe9ezXdKyGkY00xMEfcaTh"

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('../')

def user_login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('../dashboard/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'nonprofit/login.html')

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
           
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
       

    return render(request, 'nonprofit/register.html',
                  {'user_form': user_form,'registered': registered})


def index(request):
    return render(request, 'nonprofit/index.html')


def aboutus(request):
    return render(request, 'nonprofit/aboutus.html')

def info(request):
    return render(request, 'nonprofit/information.html')


def request_box(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        state = request.POST['state']
        city = request.POST['city']
        address = request.POST['address']
        sub_group = request.POST['sub_group']
        sub_requests = RequestDonationBox.objects.create(name=name, email=email, phone=phone, state=state, city=city, address=address, sub_group=sub_group)
        sub_requests.save()
        return redirect(reverse('subsuccess', args=[name]))
    return render(request, "nonprofit/request_box.html")

def listrequest_box(request):
    requests = RequestDonationBox.objects.all()
    return render(request, "nonprofit/listrequest_box.html", {'requests':requests})

def request_env(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        state = request.POST['state']
        city = request.POST['city']
        address = request.POST['address']
        sub_group = request.POST['sub_group']
        sub_requests = RequestEnvelope.objects.create(name=name, email=email, phone=phone, state=state, city=city, address=address, sub_group=sub_group)
        sub_requests.save()
        return redirect(reverse('subsuccess', args=[name]))
    return render(request, "nonprofit/request_env.html")

def listrequest_env(request):
    requests = RequestEnvelope.objects.all()
    return render(request, "nonprofit/listrequest_env.html", {'requests':requests})


def clothing(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        state = request.POST['state']
        city = request.POST['city']
        address = request.POST['address']
        cc = request.POST['cc']
        date = request.POST['date']
        time = request.POST['time']
        sub_requests = ClothingDonation.objects.create(name=name, email=email, phone=phone, state=state, city=city, address=address, cc=cc, date=date, time=time)
        sub_requests.save()
        return redirect(reverse('subsuccess', args=[name]))
    return render(request, "nonprofit/clothing.html")

def list_clothing(request):
    requests = ClothingDonation.objects.all()
    return render(request, "nonprofit/list_clothing.html", {'requests':requests})


def room(request, room_name):
    return render(request, 'nonprofit/room.html', {'room_name': room_name })

def cashindex(request):
    return render(request, 'nonprofit/cashindex.html')

def charge(request):


	if request.method == 'POST':
		print('Data:', request.POST)

		amount = int(request.POST['amount'])

		customer = stripe.Customer.create(
			email=request.POST['email'],
			name=request.POST['nickname'],
			source=request.POST['stripeToken']
			)

		charge = stripe.Charge.create(
			customer=customer,
			amount=amount*100,
			currency='sgd',
			description="Donation"
			)

	return redirect(reverse('success', args=[amount]))


def successMsg(request, args):
	amount = args
	return render(request, 'nonprofit/success.html', {'amount':amount})

def user_profile(request):
    def get(self, request, pk, *args, **kwargs):
        profile = User.objects.get(pk=pk)
        user = profile.username
        context = {
            'user': user,
            'profile': profile,
        }
    return render(request, 'nonprofit/dashboard.html')

def subsuccessMsg(request, args):
	name = args
	return render(request, 'nonprofit/subsuccess.html', {'name':name})