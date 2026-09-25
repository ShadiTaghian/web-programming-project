from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from enrollment.models import Student
# Create your views here.

def enroll_student(request):
    template = loader.get_template('enroll.html')
    return HttpResponse(template.render())

def register_student(request):
    success = False
    if request.method == 'POST':
        Student.objects.create(
            name=request.POST.get('name', ''),
            email=request.POST.get('email', ''),
            phone=request.POST.get('phone', ''),
            address=request.POST.get('address', ''),
            city=request.POST.get('city', ''),
            state=request.POST.get('state', ''),
            zip_code=request.POST.get('zip_code', ''),
            country=request.POST.get('country', ''),
        )
        success = True
    return render(request, 'register.html', {'success': success})

