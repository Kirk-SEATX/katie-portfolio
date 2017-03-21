from django.shortcuts import render
from work_app.models import Project

# Create your views here.


def index(request):
    works = Project.objects.all()
    return render(request, 'index.html', {'works':works})

