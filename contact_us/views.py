from django.shortcuts import render
from .models import ContactUs
from .forms import ContactUsForm

from django.http import HttpResponseRedirect


# Create your views here.


def contact_us(request):
    form = ContactUsForm()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactUsForm()
            return HttpResponseRedirect('success')
        else:
            form = ContactUsForm()
            return HttpResponseRedirect('success')

    return render(request, 'contact_us/contact_us_form.html', {'form': form })


def success(request):
	# Message if subscription goes ahead
	return render(request, 'newsletter/success.html')


def error(request):
	# Message if subscription fails
	return render(request, 'newsletter/error.html')
