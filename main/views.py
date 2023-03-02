from django.shortcuts import render
from .models import Request, Region, District
import requests
from django.conf import settings
from django.shortcuts import HttpResponseRedirect
from .forms import NewRequestForm
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

def home_view(request):

    args = {
        'regions': Region.objects.all(),
        'form': NewRequestForm(),
    }
    return render(request, 'home.html', args)



def district_detail_view(request, district_id):
    args = {
        'district': District.objects.get(id=district_id),
        'form': NewRequestForm(),
    }
    return render(request, 'district.html', args)


def new_request(request):
    if request.method == 'POST':
        form = NewRequestForm(request.POST)
        if form.is_valid():
                new_request = form.save()
                new_request.save()
                messages.success(request, "Ваша заявка успешно отправлена!")
                message = render_to_string('mail/email_request_notification.html', {
                    'new_request': new_request
                })
                to_email = "uebashin@gmail.com"
                to_email_yariq = "yaroslav_kucc@mail.ru"
                mail_subject = "Новая заявка на экскурсию от " + new_request.name
                email = EmailMessage(
                    mail_subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    to=[to_email]
                )
                email.fail_silently = False
                email.send()

                email_yariq = EmailMessage(
                    mail_subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    to=[to_email_yariq]
                )
                email_yariq.fail_silently = False
                email_yariq.send()
        else:
                print(form.errors)

    return  HttpResponseRedirect(request.META['HTTP_REFERER'])