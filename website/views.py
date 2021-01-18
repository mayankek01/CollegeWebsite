from django.shortcuts import render
from . models import Teachingstaff
from . models import Product
from . models import nonTeachingstaff
from . models import others
from . models import collegenotices


def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')


def staffsel(request):
    return render(request,'staffsel.html')


def staff(request):

    tstaff = Teachingstaff.objects.all()

    return render(request, 'staff.html', {'tstaff' : tstaff})


def nonteaching(request):

    nstaff = nonTeachingstaff.objects.all()

    return render(request,'nonteaching.html', {'nstaff' : nstaff})


def other(request):

    ostaff = others.objects.all()
    
    return render(request,'others.html', {'ostaff' : ostaff}) 


def course(request):
    return render(request,'course.html')


def notice(request):

    notices = collegenotices.objects.all()

    return render(request,'notice.html', {'notices' : notices})