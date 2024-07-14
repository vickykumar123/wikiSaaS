from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit

def home_view(request,*args, **kwargs):
    queryset = PageVisit.objects.all()
    
    return render(request)