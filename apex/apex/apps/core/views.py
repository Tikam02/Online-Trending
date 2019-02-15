from django.shortcuts import render

from apex.apps.services.models import Service 

def status(request):
    services = Service.objects.all()
    return render(request,'core/status.html',{
        'services':services
    })