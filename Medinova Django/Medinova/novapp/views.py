from django.shortcuts import render
from .forms import AppoinmentForms
from django.contrib import messages
from django.core.mail import EmailMessage
from django.http import HttpResponse

# Create your views here.

def view_home(request):
    resp=render(request,'novapp/home.html')
    return resp

def view_about(request):
    resp=render(request,'novapp/about.html')
    return resp

def view_service(request):
    if request.method=='GET':
        frm_unbound=AppoinmentForms()
        d1={'forms':frm_unbound}
        resp=render(request,'novapp/service.html',context=d1)
        return resp 
    elif request.method=='POST':
        frm_bound=AppoinmentForms(request.POST)
        if frm_bound.is_valid():  # Server Side Validation
            frm_bound.save()
            messages.success(request,'Appointment Sent SuccessFully!!')
            return render(request,'novapp/service.html')
        else:
            messages.warning(request,'Appointment Sent Failed!!')
            return render(request,'novapp/service.html')

def view_pricing(request):
    resp=render(request,'novapp/pricing.html')
    return resp

def view_contact(request):
    resp=render(request,'novapp/contact.html')
    return resp

def view_sendmail(request):
    if request.method=='GET':
        return render(request,'novapp/sendmail.html')
    elif request.method=='POST':
        subject = request.POST.get("txtsubject", "NA")
        message = request.POST.get("txtmessage", "NA")
        from_email = request.POST.get("txtemail", "NA")
        if subject and message and from_email:
            email_message=EmailMessage(subject, message, from_email, [from_email])
            email_message.send()
            return HttpResponse("Email Sent SuccessFully!!")
        else:
            return HttpResponse("Make sure all fields are entered and valid.")





