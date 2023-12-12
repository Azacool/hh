from django.shortcuts import render
from .models import Content

def main(request):
    contents = Content.objects.all()
    for content in contents:
        print(content.image)
    return render(request,'index.html',{'contents':contents})

def contact(request):
    contact = Content.objects.all()
    return render(request,'contact.html',{'contact':contact})

def topic_listing(request):
    topic_listing = Content.objects.all()
    return render(request,'topics-listing.html',{'topic_listing':topic_listing})