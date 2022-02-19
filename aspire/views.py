from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import ApplyForm
from .models import Apply
from django.conf import settings
import smtplib
import ssl
from .serializers import ApplySerializer
from rest_framework import status

# from django.core.mail import send_mass_mail, EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create your views here.

def home(request):
    return render(request, 'index.html')

def apply(request):

    form = ApplyForm()

    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)

        if form.is_valid():
            # form.save()

            pwd = "ybnl12345@"
            subject = 'Welcome to Aspire'
            body = f"Hi {form['first_name'].value().capitalize()} {form['last_name'].value().capitalize()}, thank you for registering on Aspire always"
            sender_email = "seyiclass@gmail.com"
            receiver_email = form['email_address'].value()

            # Create a multipart message and set headers
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = subject
            # message["Bcc"] = receiver_email  # Recommended for mass emails

            # Add body to email
            message.attach(MIMEText(body, "plain"))
            text = message.as_string()

            # Log in to server using secure context and send email
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, pwd)
                server.sendmail(sender_email, receiver_email, text)

            form.save()
            return redirect('/')

        else:
            print(form.is_valid())
            print(form.errors)
            form = ApplyForm(request.POST)
    else:
        form = ApplyForm()

    return render(request, 'apply.html', {'form' : form})


class ApplyView(APIView):

    def get(self, request, number):
        # response = dict()

        # number = request.data.get('number')
        try:
            item = Apply.objects.get(mobile_number=number)
            serializer = ApplySerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        except:
            return Response({
                "status": "failed",
                "application status" : "pending",
                "number" : "you entered the wrong number"
            })