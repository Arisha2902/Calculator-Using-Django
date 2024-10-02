from django.shortcuts import render, HttpResponse
from app.models import *
from .forms import calc


# Create your views here.
def home(req):
    try:
      return HttpResponse("hello")
    except  Exception as e:
        return HttpResponse(e)

def calcultor(req):
    out=0
    op_CHOICES = [
    ('+', 'add'),
    ('-', 'sub'),
    ('*', 'mul'),

]
    # op_CHOICES1=tuple( op_CHOICES)
    if req.method == "POST":
       fm=calc(req.POST)
       if fm.is_valid():
         n1= int(req.POST['num1'])
         n2= int(req.POST['num2'])
         op=(req.POST['operator1'])
       if op =="+":
          out=n1+n2
       elif op =="-":
          out=n1-n2
       elif op =="*":
          out=n1-n2
      #  op=(n1+n2)
    else:
      fm=calc()
    return render(req,"home.html",{'form':fm, 'output':out})

    # return render(req, "utube.html", {'form': fm, 'out': op})

      