from django.shortcuts import render
from .models import usermsg, indexmodel, booking, doctordata, department, About


# Create your views here.


def index(request):
    img = indexmodel.objects.all()

    return render(request,'index.html',{'img':img})


def about(request):
    img = About.objects.all()
    return render(request,'about.html',{'img': img})


def bookings(request):
    if request.method == 'POST':
        Patientname = request.POST.get('Patientname')
        Phonenumber = request.POST.get('Phonenumber')
        EmailId = request.POST.get('Email')
        Doctorname = request.POST.get('Doctorname')
        Bookingdate = request.POST.get('Bookingdate')


        obj1 = booking(Patientname=Patientname, Phonenumber=Phonenumber,
                       EmailId=EmailId, Doctorname=Doctorname, Bookingdate=Bookingdate)
        obj1.save()

    doctors = doctordata.objects.all()
    return render(request,'booking.html',{'doctors': doctors})


def doctor(request):
    data = doctordata.objects.all()

    return render(request,'doctor.html',{'data':data})


def depart(request):
    try:
        departments = department.objects.all()
        context = {'departments': departments}
    except department.DoesNotExist:
        context = {'departments': None}
    return render(request, 'department.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        msg = request.POST.get('issues')
        obj = usermsg(name=name,email=email,phone=phone,subject=subject,msg=msg)
        obj.save()
    return render(request,'contact.html')

