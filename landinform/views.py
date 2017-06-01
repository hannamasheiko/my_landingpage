
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import SignUpForm

# Create your views here.
def home(request):
    title = "welcome"
    form = SignUpForm(request.POST or None)
    context = {
        'title': title,
        'form': form,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        full_name =  form.cleaned_data.get('full_name')
        if not full_name:
            full_name = "new full name"
        instance.full_name = full_name
        instance.email = form.cleaned_data.get('email')
        subject = "Some sub"
        message = "Thank you for order"
        from_email = settings.EMAIL_HOST_USER
       # to_email = 'annatestit@gmail.com'

        send_mail(subject, message, from_email,
                  ['hannamasheiko@gmail.com'], fail_silently=True)
       # if not instance.full_name:
         #   instance.full_name = "Anonim"
        instance.save()
        context = {
            'title': "Thank you"
        }

    return render(request, "landinform/index.html", context)