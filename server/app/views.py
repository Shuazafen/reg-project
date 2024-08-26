from django.shortcuts import render, get_object_or_404
from django.conf.urls.static import static
from .models import *

def home(request):
    form = People.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone-number']
        message = request.POST['message']
        contact_info = contact(name=name, phone=phone, message=message)
        contact_info.save()
    else:
        print('Not sent')
    return render(request, 'index.html',{'form':form})

# Create your views here.
