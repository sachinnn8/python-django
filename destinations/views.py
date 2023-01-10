from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader



from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.urls import reverse
from accounts.models import Profile
from .forms import *
from .models import *

from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
@login_required
def index(request):
	return render(request, "index.html")

@login_required
def home(request):
	return render(request, "index.html")

@login_required
def message(request):
	return render(request, "message.html")
		
@login_required
def contact(request):
	return render(request, "contact.html")

@login_required
def listing(request):
	return render(request, "listing.html")

@login_required
def admin_dashboard(request):
	return render(request, "admin_dashboard.html")

@login_required
def destinations_place(request):
	form = DestinationForm()
	if request.method == 'POST':
		form = DestinationForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			
			return redirect('admin_dashboard')
	else:
		context = {
		'form': form,
		}

		return render(request, 'add_destinations.html', context)



@login_required
def explore(request):
	query = request.GET.get("q")
	context = {}
	
	if query:
		destination = Destinations.objects.filter(Q(name__icontains=query))

		#Pagination
		paginator = Paginator(destination, 5)
		page_number = request.GET.get('page')
		destinations_paginator = paginator.get_page(page_number)

		context = {
				'destination': destinations_paginator,
				'destinations': destination
			}
	
	template = loader.get_template('explore.html')
	
	return HttpResponse(template.render(context, request))
	
		


@login_required	
def destination_list(request):
    destinations = Destinations.objects.all().order_by('-Created_date')
    context = {'destinations': destinations}
    return render(request, 'destination_list.html', context)







@login_required	
def category_destinations_religious(request):
    destinations = Destinations.objects.filter(category="Religious").order_by('-Created_date')
    context = {'destinations': destinations}
    return render(request, 'category_destinations.html', context)

@login_required	
def category_destinations_hilly(request):
    destinations = Destinations.objects.filter(category="Hilly").order_by('-Created_date')
    context = {'destinations': destinations}
    return render(request, 'category_destinations.html', context)


@login_required	
def category_destinations_mountain(request):
    destinations = Destinations.objects.filter(category="Mountain").order_by('-Created_date')
    context = {'destinations': destinations}
    return render(request, 'category_destinations.html', context)

@login_required	
def category_destinations_terai(request):
    destinations = Destinations.objects.filter(category="Terai").order_by('-Created_date')
    context = {'destinations': destinations}
    return render(request, 'category_destinations.html', context)


@login_required	
def category_destinations_famous(request):
    destinations = Destinations.objects.filter(category="FamousDestination").order_by('-Created_date')
    context = {'destinations': destinations}
    return render(request, 'category_destinations.html', context)

@login_required	
def category_destinations_jungle(request):
    destinations = Destinations.objects.filter(category="JungleSafari").order_by('-Created_date')
    context = {'destinations': destinations}
    return render(request, 'category_destinations.html', context)





@login_required
def admin_destination_list(request):
	destinations = Destinations.objects.all().order_by('-Created_date')
	context = {'destinations': destinations}
	return render(request, 'admin_destination_list.html', context)

@login_required
def destination_detail(request, destination_id):
	user=request.user
	destination = Destinations.objects.get(id=destination_id)
	booking_status = Bookings.objects.filter(user=user, destinations=destination).exists()
	context = {'destinations': destination, 'booking_status': booking_status}
	return render(request, 'destination_details.html', context)

@login_required
def admin_destination_detail(request, destination_id):
	destination = Destinations.objects.get(id=destination_id)
	context = {'destinations': destination}
	return render(request, 'admin_destination_detail.html', context)

@login_required
def delete_destination(request, destination_id):
	destination = Destinations.objects.filter(id=destination_id).delete()
	return redirect('admin_destination_list')

@login_required
def update_destination(request, destination_id):
	destination = Destinations.objects.get(id=destination_id)


	if request.method == 'POST':
		form = EditDestinationForm(request.POST, request.FILES)
		if form.is_valid():
			destination.name = form.cleaned_data.get('name')
			destination.picture = request.FILES.get('picture')
			destination.description = form.cleaned_data.get('description')
			destination.save()
			return redirect('admin_destination_list')
	else:
		form = EditDestinationForm()

	context = {
		'form':form,
	}

	return render(request, 'update_destination.html', context)
	


@login_required
def bookings(request, destination_id):
	user = request.user
	destination_book = Destinations.objects.get(id=destination_id)
	booked = Bookings.objects.filter(user=user, destinations=destination_book)

	if not booked:
		book = Bookings.objects.create(user=user, destinations=destination_book)
		

	else:
		Bookings.objects.filter(user=user, destinations=destination_book).delete()
		


	return redirect('destination_list')

@login_required
def messages(request):
	user= request.user
	form= MessageForm()
	if request.method == 'POST':
		form= MessageForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.SUCCESS, 'Message Send Successfully')

	else:
		context = {
		'form': MessageForm()
		}

		return render(request, 'messages.html', context)


@login_required
def mesge(request):
	user = request.user
	if request.method == 'POST':
		form = MesgeForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data.get('name')
			mail = form.cleaned_data.get('mail')
			number = form.cleaned_data.get('number')
			mesge = form.cleaned_data.get('mesge')
			Messages.objects.create(user=user, name=name, mail=mail, number=number, mesge=mesge)
			return redirect('index')
	else:
		form = MesgeForm()
	
	context = {
		'form':form,
	}

	return render(request, 'message.html', context)


@login_required
def admin_messages(request):
	mesges= Messages.objects.all().order_by('-date')
	context = {'mesges':mesges}
	return render(request, 'admin_message.html', context)


@login_required
def admin_bookings(request):
	bookings= Bookings.objects.all().order_by('-date')
	context = {'bookings':bookings}
	return render(request, 'admin_bookings.html', context)


@login_required
def galary(request):
	form = GalaryForm(request.POST or None, request.FILES or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.SUCCESS, 'Galary added Successfully')
			return redirect('admin_dashboard')
	else:
		context = {
		'form': GalaryForm,
		}

		return render(request, 'add_destinations.html', context)

@login_required
def religious_tour(request):
	return render(request, "religious_tour.html")

@login_required
def hilly_tour(request):
	return render(request, "hilly_tour.html")

@login_required
def mountain_tour(request):
	return render(request, "mountain_tour.html")

@login_required
def terai_tour(request):
	return render(request, "terai_tour.html")

@login_required
def pokhara_tour(request):
	return render(request, "pokhara_tour.html")

@login_required
def jungle_safari(request):
	return render(request, "jungal_safari.html")