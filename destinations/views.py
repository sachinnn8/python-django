from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


from django.contrib.auth.decorators import login_required

from django.urls import reverse
from accounts.models import Profile



# Create your views here.
@login_required
def index(request):
	return render(request, "index.html")
		
@login_required
def contact(request):
	return render(request, "contact.html")

@login_required
def listing(request):
	return render(request, "listing.html")