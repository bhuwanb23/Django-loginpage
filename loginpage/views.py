from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

# Create your views here.
def home(request):
    return render(request,'index.html')

def person_form_view(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        person = Person(first_name=firstname, last_name=lastname, address=address, email=email, password=password, username=username)
        person.save()
        print("worked")
        return HttpResponse('Person created successfully!')
    else:
        print("not worked")
        return render(request, 'index.html')