from django.urls import path
from destinations.views import index,contact,listing


urlpatterns = [
   	path('', index, name='index'),
   	path('contact/', contact, name='contact'),
   	path('listing/', listing, name='listing'),
]