from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')
def add(request):

    x=request.POST["t1"]
    y=request.POST["t2"]
    i=int(x)
    j=int(y)
    z=i+j
    res=HttpResponse("""<body bgcolor=yellow>THE SUM OF TWO VALUES IS::</body>"""+str(z))
    return res