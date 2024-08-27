from django.shortcuts import render, get_object_or_404
from django.conf.urls.static import static
from .models import *

def home(request):
    form = People.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        birth = request.POST['birth']
        member_rccg = request.POST['member_rccg']
        whatsapp_no = request.POST['whatsapp_no']
        referee = request.POST['referee']
        attended_prev = request.POST['attended_prev']
        suggestions = request.POST['suggestions']
        form_info = People(name=name, phone=phone, birth=birth, member_rccg=member_rccg, whatsapp_no=whatsapp_no, referee=referee, attended_prev=attended_prev, suggestions=suggestions)
        form_info.save()
    else:
        print('Not sent')
    return render(request, 'index.html',{'form':form})

# Create your views here.
