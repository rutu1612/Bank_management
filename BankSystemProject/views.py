from django.shortcuts import render

from twilio.rest import Client
from django.conf import settings

def index(request):
    return render(request, "index.html")

def sms(request):
    to = '+919370455057'
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    response = client.messages.create(body='Request sent for password reset', to=to, from_=settings.TWILIO_PHONE_NUMBER)
    return render(request, 'pass.html')
