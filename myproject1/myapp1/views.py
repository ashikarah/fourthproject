from django.shortcuts import render
#from .models import place
from .models import teams

def demo(request):
    obj = teams.objects.all()
    return render(request, "index.html", {'val': obj})


#
# def demo1(request):
#     obj1 = teams.objects.all()
#     return render(request, "index.html", {'val1': obj1})

