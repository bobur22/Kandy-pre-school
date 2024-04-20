from django.shortcuts import render, redirect
from django.template import loader
from .forms import CareerForm, ContactForm, ApplicationForm
from .models import Career
from django.core.mail import send_mail
import requests
import vonage
from django.contrib.auth.decorators import login_required
from .tasks import send_mail_task


def home_view(request):
    return render(request, 'index.html')


def about_view(request):
    return render(request, 'about.html')


def team_view(request):
    return render(request, 'team.html')


def program_view(request):
    return render(request, 'programs.html')


def enroll_view(request):
    error_m = None
    form = ApplicationForm()
    if request.method == 'POST':
        p_fname = request.POST['parent_fname']
        email = request.POST['email']
        form = ApplicationForm(request.POST)
        message_1 = f"Hello, Dear {p_fname},\nYour report sent."
        if form.is_valid():
            error_m = "login"
            x = form.save()
            send_mail_task.delay('Enrollment Form', message_1, recipient_list=[email], html_m=loader.render_to_string('email/enrollment_email.html', context={
                    'form': x,
                    'email': email,
                })
            )
            form.save()
            return redirect("enrollment-p")
        else:
            error_m = "error"

    return render(request, 'enrollment.html', context={'form': form, 'error_m': error_m})


def career_view(request):
    form = CareerForm()
    if request.method == 'POST':
        f_name = request.POST['f_name']
        email = request.POST['email']
        form = CareerForm(request.POST)
        message_1 = f"Hello, Dear {f_name},\nYour report sent."
        if form.is_valid():
            form.save()
            send_mail_task.delay('Career Form', message_1, recipient_list=[email],
                                 html_m=loader.render_to_string('email/email.html', context={
                                     'first_name': f_name,
                                     'email': email,
                                 }))
            return redirect("career-p")

    return render(request, 'careers.html', context={'form': form})


def contact_view(request):
    form = ContactForm()  # Instantiate the form
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            f_name = form.cleaned_data['f_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['p_number']  # Field name corrected
            cf_name = form.cleaned_data['c_f_name']  # Field name corrected
            c_date = form.cleaned_data['c_date']
            a_date = form.cleaned_data['a_date']
            text = form.cleaned_data['text']

            message_1 = f"Hello, Dear {f_name},\nYour detail sent."

            # Send email
            send_mail_task.delay('Contact Form', message_1, recipient_list=[email],
                                 html_m=loader.render_to_string('email/contact_email.html',
                                                                context={'f_name': f_name, 'email': email,
                                                                         'a_date': a_date})
                                 )

            # Send message to Telegram
            text1 = "Contact Form to the Kandy pre-school: \n"
            text1 += f"Full Name: {f_name}\n"
            text1 += f"Email: {email}\n"
            text1 += f"Phone number: {phone}\n"
            text1 += f"Child's Full Name: {cf_name}\n"
            text1 += f"Date: {c_date}\n"
            text1 += f"Date: {a_date}\n"
            token = '6982864288:AAHaZJUWTRzL3YBtRLf68WiCWgaVGh6Ko8E'  # Replace with your Telegram Bot token
            id = "1292573250"  # Replace with your Telegram Chat ID
            url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id='
            requests.get(url + id + '&text=' + text1)

            return redirect('contact-p')

    return render(request, 'contact.html', context={'form': form})
