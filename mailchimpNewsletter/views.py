from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect

from django.conf import settings
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError

from .forms import SubscriberForm
from .models import Subscriber

# Tutorial took from 
# https://www.geeksforgeeks.org/create-newsletter-app-using-mailchimp-and-django/
# with some adjusts for suit the project

# Mailchimp Settings
api_key = settings.MAILCHIMP_API_KEY
server = settings.MAILCHIMP_DATA_CENTER
list_id = settings.MAILCHIMP_EMAIL_LIST_ID


# function to manage subscriber
def subscribeToNewsLetter(request):
	if request.method == "POST":

		# getting users input from the form
		email = request.POST['email']
		name = request.POST['name']


		# initializing the mailchimp client with api key
		mailchimpClient = Client()
		mailchimpClient.set_config({
			"api_key": api_key,

		})
		# info register in audience
		userInfo = {
			"email_address": email,
			"status": "subscribed",
			"fields": {
				"NAME": name,
			}
		}

		#This is my adition to save the subscribers to a local model as backup.
		subscriber_form = SubscriberForm(request.POST)
		if subscriber_form.is_valid():
			print(email)
			print(name)
			subscriber_email = subscriber_form.cleaned_data['email']
			subscriber_name = subscriber_form.cleaned_data['name']
			subscriber_form.save()

		try:
			# adding member to mailchimp audience list
			mailchimpClient.lists.add_list_member(list_id, userInfo)
			return HttpResponseRedirect('success')
		except ApiClientError as error:
			print(error.text)
			return HttpResponseRedirect('error')

	return self.request.path


def success(request):
	# Message if subscription goes ahead
	return render(request, 'newsletter/success.html')


def error(request):
	# Message if subscription fails
	return render(request, 'newsletter/error.html')
