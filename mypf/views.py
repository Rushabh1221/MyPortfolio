from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import Contact

#Portfolio View:
def portfolio(request):
    return render(request, 'mypf/portfolio.html')


#Contact View:
def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        form = Contact(email=email, subject=subject, message=message)

        # Saving Form data to Database
        messages.success(request, 'Your message is Sent :) ')
        form.save()

        return render(request, 'mypf/contact.html')
    else:
        return render(request, 'mypf/contact.html')
