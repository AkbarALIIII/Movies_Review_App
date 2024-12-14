from django.shortcuts import render,HttpResponse
from .models import News
# Create your views here.
def news(request):
    newss=News.objects.all().order_by('date')
    return render(request,'news.html',{'newss':newss})