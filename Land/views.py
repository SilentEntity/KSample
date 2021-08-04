from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
import os

dir_path = os.path.dirname(os.path.realpath(__file__))


# Create your views here.

def index(request):
    return render(request, template_name='{}/template/index.html'.format(dir_path))


def status(request):
    try:
        total_users = User.objects.all().count()
    except Exception as e:
        total_users = 0
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return JsonResponse({"status": "Running",
                         "version": 0.1,
                         "request": request.method,
                         "total-users": total_users,
                         "your-ip": ip})
