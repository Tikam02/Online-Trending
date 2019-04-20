from .models import Service

def services(request):
    return {
        'services_slugs' : Service.objects.all()
    }