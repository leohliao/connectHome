import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# function based view
def home(request):
    num = random.randint(0, 100000)
    some_list = [num, random.randint(0, 100000), random.randint(0, 100000)]

    context = {
        "bool_item": False,
        "num": num,
        "some_list": some_list
    }
    return render(request, "base.html", context )
