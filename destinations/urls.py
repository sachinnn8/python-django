from django.urls import path
from destinations.views import *


urlpatterns = [
   	path('', index, name='index'),
   	path('home/', home, name='home'),
   	path('message/', message, name='message'),
   	path('contact/', contact, name='contact'),
   	path('explore/', explore, name='explore'),
   	path('listing/', listing, name='listing'),
   	path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
   	path('destinations_place/', destinations_place, name='destinations_place'),
   	path('destination_list/', destination_list, name='destination_list'),
   	path('<uuid:destination_id>/destination_detail', destination_detail, name='destination_detail'),
   	path('<uuid:destination_id>/bookings', bookings, name='bookings'),
   	path('religious_tour/', religious_tour, name='religious_tour'),
   	path('hilly_tour/', hilly_tour, name='hilly_tour'),
   	path('mountain_tour/', mountain_tour, name='mountain_tour'),
   	path('terai_tour/', terai_tour, name='terai_tour'),
   	path('pokhara_tour/', pokhara_tour, name='pokhara_tour'),
   	path('jungle_safari/', jungle_safari, name='jungle_safari'),
   	path('admin_destination_list/', admin_destination_list, name='admin_destination_list'),
   	path('<uuid:destination_id>/admin_destination_detail', admin_destination_detail, name='admin_destination_detail'),
   	path('<uuid:destination_id>/delete_destination', delete_destination, name='delete_destination'),
   	path('<uuid:destination_id>/update_destination', update_destination, name='update_destination'),
   	path('messages/', mesge, name='mesge'),
   	path('admin_messages/', admin_messages, name='admin_messages'),
   	path('admin_bookings/', admin_bookings, name='admin_bookings'),


   	path('category_destinations_religious/', category_destinations_religious, name='category_destinations_religious'),
   	path('category_destinations_hilly/', category_destinations_hilly, name='category_destinations_hilly'),
   	path('category_destinations_mountain/', category_destinations_mountain, name='category_destinations_mountain'),
   	path('category_destinations_terai/', category_destinations_terai, name='category_destinations_terai'),
   	path('category_destinations_famous/', category_destinations_famous, name='category_destinations_famous'),
   	path('category_destinations_jungle/', category_destinations_jungle, name='category_destinations_jungle'),



]