from django.urls import path
from .views import main,contact,topic_listing

urlpatterns = [
    path('',main),
    path('contact.html',contact),
    path('topics-listing.html',topic_listing),
]