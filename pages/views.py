from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect

from emrebeysite.settings import EMAIL_HOST_USER
from pages.forms import PostForm, PostForm2, PostForm3
from pages.models import *
from templates import *
from django.template import loader
from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.

def index(request):
    print("kk")

    if request.POST:
        form = PostForm(request.POST)



        if form.is_valid():
            # "formmail = form.cleaned_data["email"]
            # boardtype = form.cleaned_data['boardtype']"
            subject = form.cleaned_data['name']
            message = form.cleaned_data['subject'] + "\n Mail :" + form.cleaned_data['email'] + "\n telefon : " + \
                      form.cleaned_data['phone']
            # send_mail(subject, message, formmail, [formmail])
            form.save()

            send_mail(

                subject,
                message,
                EMAIL_HOST_USER,
                ['info.dogukandugun@gmail.com','gamze@firmaklinigi.com'],
                fail_silently=False,
            )

            messages.success(request, "basarılı")



        else:
            messages.error(request, "hata")
            print("form hata")

    form = PostForm()

    return render(request, 'index.html', {'form': form})


def firmaklinigihakkinda(request):
    print("kk")

    if request.POST:
        form = PostForm(request.POST)

        if form.is_valid():
            # "formmail = form.cleaned_data["email"]
            # boardtype = form.cleaned_data['boardtype']"
            subject = form.cleaned_data['name']
            message = form.cleaned_data['subject'] + "\n Mail :" + form.cleaned_data['email'] + "\n telefon : " + \
                      form.cleaned_data['phone']
            # send_mail(subject, message, formmail, [formmail])
            form.save()

            send_mail(

                subject,
                message,
                EMAIL_HOST_USER,
                ['info.dogukandugun@gmail.com','gamze@firmaklinigi.com'],
                fail_silently=False,
            )

            messages.success(request, "basarılı")



        else:
            messages.error(request, "hata")
            print("form hata")

    form = PostForm()

    return render(request, 'firma-kliniği.html', {'form': form})

def tarihce(request):
    print("kk")

    if request.POST:
        form = PostForm(request.POST)

        if form.is_valid():
            # "formmail = form.cleaned_data["email"]
            # boardtype = form.cleaned_data['boardtype']"
            subject = form.cleaned_data['name']
            message = form.cleaned_data['subject'] + "\n Mail :" + form.cleaned_data['email'] + "\n telefon : " + \
                      form.cleaned_data['phone']
            # send_mail(subject, message, formmail, [formmail])
            form.save()

            send_mail(

                subject,
                message,
                EMAIL_HOST_USER,
                ['info.dogukandugun@gmail.com','gamze@firmaklinigi.com'],
                fail_silently=False,
            )

            messages.success(request, "basarılı")



        else:
            messages.error(request, "hata")
            print("form hata")

    form = PostForm()

    return render(request, 'tarihce.html', {'form': form})


def iletisim(request):
    print("kk")

    if request.POST:
        form = PostForm2(request.POST)

        if form.is_valid():
            # "formmail = form.cleaned_data["email"]
            # boardtype = form.cleaned_data['boardtype']"
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message'] +"\n İsim : "+form.cleaned_data['name']+ "\n Mail :" + form.cleaned_data['email'] + "\n telefon : " + form.cleaned_data['phone']
            # send_mail(subject, message, formmail, [formmail])
            form.save()

            send_mail(

                subject,
                message,
                EMAIL_HOST_USER,
                ['info.dogukandugun@gmail.com','gamze@firmaklinigi.com'],
                fail_silently=False,
            )

            messages.success(request, "basarılı")



        else:
            messages.error(request, "hata")
            print("form hata")

    form = PostForm2()

    return render(request, 'contact.html', {'form': form})


def hizmetlerimiz(request):
    print("kk")

    if request.POST:
        form = PostForm(request.POST)

        if form.is_valid():
            # "formmail = form.cleaned_data["email"]
            # boardtype = form.cleaned_data['boardtype']"
            subject = form.cleaned_data['name']
            message = form.cleaned_data['subject'] + "\n Mail :" + form.cleaned_data['email'] + "\n telefon : " + \
                      form.cleaned_data['phone']
            # send_mail(subject, message, formmail, [formmail])
            form.save()

            send_mail(

                subject,
                message,
                EMAIL_HOST_USER,
                ['info.dogukandugun@gmail.com','gamze@firmaklinigi.com'],
                fail_silently=False,
            )

            messages.success(request, "basarılı")



        else:
            messages.error(request, "hata")
            print("form hata")

    form = PostForm()

    return render(request, 'hizmetlerimiz.html', {'form': form})


def ar_ge_hizmetleri(request):
    print("kk")

    if request.POST:
        form = PostForm(request.POST)

        if form.is_valid():
            # "formmail = form.cleaned_data["email"]
            # boardtype = form.cleaned_data['boardtype']"
            subject = form.cleaned_data['name']
            message = form.cleaned_data['subject'] + "\n Mail :" + form.cleaned_data['email'] + "\n telefon : " + \
                      form.cleaned_data['phone']
            # send_mail(subject, message, formmail, [formmail])
            form.save()

            send_mail(

                subject,
                message,
                EMAIL_HOST_USER,
                ['info.dogukandugun@gmail.com','gamze@firmaklinigi.com'],
                fail_silently=False,
            )

            messages.success(request, "basarılı")



        else:
            messages.error(request, "hata")
            print("form hata")

    form = PostForm()

    return render(request, 'ar-ge-hizmetleri.html', {'form': form})


def destek_hizmetleri(request):
    print("kk")

    if request.POST:
        form = PostForm3(request.POST)

        if form.is_valid():
            # "formmail = form.cleaned_data["email"]
            # boardtype = form.cleaned_data['boardtype']"
            subject = "Randevu Talebi"
            message = "İsim : " + form.cleaned_data['name'] + "\n Mail :" + \
                      form.cleaned_data['email'] + "\n telefon : " + form.cleaned_data['phone']
            # send_mail(subject, message, formmail, [formmail])
            form.save()

            send_mail(

                subject,
                message,
                EMAIL_HOST_USER,
                ['info.dogukandugun@gmail.com','gamze@firmaklinigi.com'],
                fail_silently=False,
            )

            messages.success(request, "basarılı")



        else:
            messages.error(request, "hata")
            print("form hata")

    form = PostForm3()

    return render(request, 'destek-hizmetleri.html', {'form': form})


def genel_hibe_ve_tesvik_danismanligi(request):
    print("kk")

    if request.POST:
        form = PostForm3(request.POST)

        if form.is_valid():
            # "formmail = form.cleaned_data["email"]
            # boardtype = form.cleaned_data['boardtype']"
            subject = "Randevu Talebi"
            message = "İsim : " + form.cleaned_data['name'] + "\n Mail :" + \
                      form.cleaned_data['email'] + "\n telefon : " + form.cleaned_data['phone']
            # send_mail(subject, message, formmail, [formmail])
            form.save()

            send_mail(

                subject,
                message,
                EMAIL_HOST_USER,
                ['info.dogukandugun@gmail.com','gamze@firmaklinigi.com'],
                fail_silently=False,
            )

            messages.success(request, "basarılı")



        else:
            messages.error(request, "hata")
            print("form hata")

    form = PostForm3()

    return render(request, 'genel-hibe-ve-tesvik-danismanligi.html', {'form': form})


def proje_yazim_ve_yönetimi_hizmetleri(request):
    print("kk")

    if request.POST:
        form = PostForm3(request.POST)

        if form.is_valid():
            # "formmail = form.cleaned_data["email"]
            # boardtype = form.cleaned_data['boardtype']"
            subject = "Randevu Talebi"
            message = "İsim : " + form.cleaned_data['name'] + "\n Mail :" + \
                      form.cleaned_data['email'] + "\n telefon : " + form.cleaned_data['phone']
            # send_mail(subject, message, formmail, [formmail])
            form.save()

            send_mail(

                subject,
                message,
                EMAIL_HOST_USER,
                ['info.dogukandugun@gmail.com','gamze@firmaklinigi.com'],
                fail_silently=False,
            )

            messages.success(request, "basarılı")



        else:
            messages.error(request, "hata")
            print("form hata")

    form = PostForm3()

    return render(request, 'proje-yazim-ve-yönetimi-hizmetleri.html', {'form': form})


def sirket_degerleme(request):
    print("kk")

    if request.POST:
        form = PostForm3(request.POST)

        if form.is_valid():
            # "formmail = form.cleaned_data["email"]
            # boardtype = form.cleaned_data['boardtype']"
            subject = "Randevu Talebi"
            message = "İsim : " + form.cleaned_data['name'] + "\n Mail :" + \
                      form.cleaned_data['email'] + "\n telefon : " + form.cleaned_data['phone']
            # send_mail(subject, message, formmail, [formmail])
            form.save()

            send_mail(

                subject,
                message,
                EMAIL_HOST_USER,
                ['info.dogukandugun@gmail.com','gamze@firmaklinigi.com'],
                fail_silently=False,
            )

            messages.success(request, "basarılı")



        else:
            messages.error(request, "hata")
            print("form hata")

    form = PostForm3()

    return render(request, 'sirket-degerleme.html', {'form': form})

def yatirim_ve_tesvik_tanismanligi(request):
    print("kk")

    if request.POST:
        form = PostForm3(request.POST)

        if form.is_valid():
            # "formmail = form.cleaned_data["email"]
            # boardtype = form.cleaned_data['boardtype']"
            subject = "Randevu Talebi"
            message = "İsim : " + form.cleaned_data['name'] + "\n Mail :" + \
                      form.cleaned_data['email'] + "\n telefon : " + form.cleaned_data['phone']
            # send_mail(subject, message, formmail, [formmail])
            form.save()

            send_mail(

                subject,
                message,
                EMAIL_HOST_USER,
                ['info.dogukandugun@gmail.com','gamze@firmaklinigi.com'],
                fail_silently=False,
            )

            messages.success(request, "basarılı")



        else:
            messages.error(request, "hata")
            print("form hata")

    form = PostForm3()

    return render(request, 'yatirim-ve-tesvik-danismanligi.html', {'form': form})


def vergi_ve_sigorta_danismanligi(request):
    print("kk")

    if request.POST:
        form = PostForm3(request.POST)

        if form.is_valid():
            # "formmail = form.cleaned_data["email"]
            # boardtype = form.cleaned_data['boardtype']"
            subject = "Randevu Talebi"
            message = "İsim : " + form.cleaned_data['name'] + "\n Mail :" + \
                      form.cleaned_data['email'] + "\n telefon : " + form.cleaned_data['phone']
            # send_mail(subject, message, formmail, [formmail])
            form.save()

            send_mail(

                subject,
                message,
                EMAIL_HOST_USER,
                ['info.dogukandugun@gmail.com','gamze@firmaklinigi.com'],
                fail_silently=False,
            )

            messages.success(request, "basarılı")



        else:
            messages.error(request, "hata")
            print("form hata")

    form = PostForm3()

    return render(request, 'vergi-ve-sigorta-danismanligi.html', {'form': form})


def check_up_hizmeti(request):
    print("kk")

    if request.POST:
        form = PostForm3(request.POST)

        if form.is_valid():
            # "formmail = form.cleaned_data["email"]
            # boardtype = form.cleaned_data['boardtype']"
            subject = "Randevu Talebi"
            message = "İsim : " + form.cleaned_data['name'] + "\n Mail :" + \
                      form.cleaned_data['email'] + "\n telefon : " + form.cleaned_data['phone']
            # send_mail(subject, message, formmail, [formmail])
            form.save()

            send_mail(

                subject,
                message,
                EMAIL_HOST_USER,
                ['info.dogukandugun@gmail.com','gamze@firmaklinigi.com'],
                fail_silently=False,
            )

            messages.success(request, "basarılı")



        else:
            messages.error(request, "hata")
            print("form hata")

    form = PostForm3()

    return render(request, 'check-up-hizmeti.html', {'form': form})


def periyodik_arge_danismanligi(request):
    print("kk")

    if request.POST:
        form = PostForm3(request.POST)

        if form.is_valid():
            # "formmail = form.cleaned_data["email"]
            # boardtype = form.cleaned_data['boardtype']"
            subject = "Randevu Talebi"
            message = "İsim : " + form.cleaned_data['name'] + "\n Mail :" + \
                      form.cleaned_data['email'] + "\n telefon : " + form.cleaned_data['phone']
            # send_mail(subject, message, formmail, [formmail])
            form.save()

            send_mail(

                subject,
                message,
                EMAIL_HOST_USER,
                ['info.dogukandugun@gmail.com','gamze@firmaklinigi.com'],
                fail_silently=False,
            )

            messages.success(request, "basarılı")



        else:
            messages.error(request, "hata")
            print("form hata")

    form = PostForm3()

    return render(request, 'periyodik-ar-ge-danismanligi.html', {'form': form})


def ar_ge_muhasebesi_danismanlik_hizmeti(request):
    print("kk")

    if request.POST:
        form = PostForm3(request.POST)

        if form.is_valid():
            # "formmail = form.cleaned_data["email"]
            # boardtype = form.cleaned_data['boardtype']"
            subject = "Randevu Talebi"
            message = "İsim : " + form.cleaned_data['name'] + "\n Mail :" + \
                      form.cleaned_data['email'] + "\n telefon : " + form.cleaned_data['phone']
            # send_mail(subject, message, formmail, [formmail])
            form.save()

            send_mail(

                subject,
                message,
                EMAIL_HOST_USER,
                ['info.dogukandugun@gmail.com','gamze@firmaklinigi.com'],
                fail_silently=False,
            )

            messages.success(request, "basarılı")



        else:
            messages.error(request, "hata")
            print("form hata")

    form = PostForm3()

    return render(request, 'ar-ge-muhasebesi-danismanlik-hizmeti.html', {'form': form})


def portal_hizmetleri(request):
    print("kk")

    if request.POST:
        form = PostForm3(request.POST)

        if form.is_valid():
            # "formmail = form.cleaned_data["email"]
            # boardtype = form.cleaned_data['boardtype']"
            subject = "Randevu Talebi"
            message = "İsim : " + form.cleaned_data['name'] + "\n Mail :" + \
                      form.cleaned_data['email'] + "\n telefon : " + form.cleaned_data['phone']
            # send_mail(subject, message, formmail, [formmail])
            form.save()

            send_mail(

                subject,
                message,
                EMAIL_HOST_USER,
                ['info.dogukandugun@gmail.com','gamze@firmaklinigi.com'],
                fail_silently=False,
            )

            messages.success(request, "basarılı")



        else:
            messages.error(request, "hata")
            print("form hata")

    form = PostForm3()

    return render(request, 'portal-hizmetleri.html', {'form': form})

def bizimleiletisimegecin(request):

    return render(request, 'bizimleiletisimegecin.html')
