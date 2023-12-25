from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class Home(View):
    template_name = 'hostel/index.html'
    def get(self,request):
        return render(request,self.template_name)
    
def contactUs(request):
    return render(request, 'hostel/contact-us.html')

def aboutUs(request):
    return render(request, 'hostel/about-us.html')