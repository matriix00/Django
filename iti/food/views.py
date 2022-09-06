import re
from django.shortcuts import render

# Create your views here.
def foodIndex(request):
    allfood= [
        {"id":1,"name":"food1","image":"image1.png"},
        {"id":2,"name":"food2","image":"image2.png"},
        {"id":3,"name":"food3","image":"image3.png"},
        {"id":4,"name":"food4","image":"image4.png"},
        {"id":5,"name":"food5","image":"image5.png"},
        
    ]
    return render(request,"allfood.html",content={"allfood":allfood})
