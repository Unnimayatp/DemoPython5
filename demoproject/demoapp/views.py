from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
 #def home(request):
 #   return HttpResponse('HOME')
 #def about(request):
 #   return render(request, 'about.html')
 #def contact(request):
 #   return render(request, 'contact.html')
 #def details(request):
 #   return HttpResponse('DETAILS')


 #def thanks(request):
  #  return HttpResponse('THANKS')
def index(request):
    return render(request,'index.html')
def demo(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    a=x+y
    b=x-y
    c=x*y
    d=x/y
    return render(request,'result.html',{'a1':a,'b2':b,'c3':c,'d4':d})