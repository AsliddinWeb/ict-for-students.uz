from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from settings_app.models import *
from .models import *
def video_page(request):
    # Required
    SEO_SETTINGS = SeoSettings.objects.last()
    FOOTER_SETTINGS = FooterSettings.objects.last()
    SOCIAL_SETTINGS = SocialSettings.objects.all()
    LOGO_SETTINGS = LogoSettings.objects.last()
    ONE_HEADER = OneHeader.objects.all()
    TWO_HEADER = TwoHeader.objects.all()
    RIGHT_BUTTON_SETTINGS = RightButtonSettings.objects.last()
    PHONE_EMAIL_SETTINGS = PhoneEmailSettings.objects.last()

    # Main
    VIDEOS = Video.objects.all()
    page_num = request.GET.get('page', 1)
    paginator = Paginator(VIDEOS, 9)

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    ctx = {
        # Required
        'SEO_SETTINGS': SEO_SETTINGS,
        'FOOTER_SETTINGS': FOOTER_SETTINGS,
        'SOCIAL_SETTINGS': SOCIAL_SETTINGS,
        'LOGO_SETTINGS': LOGO_SETTINGS,
        'ONE_HEADER': ONE_HEADER,
        'TWO_HEADER': TWO_HEADER,
        'RIGHT_BUTTON_SETTINGS': RIGHT_BUTTON_SETTINGS,
        'PHONE_EMAIL_SETTINGS': PHONE_EMAIL_SETTINGS,

        # Main
        'VIDEOS': page_obj,
        'page_num': page_num,

    }
    return render(request, 'courses/video.html', ctx)

def slayd_page(request):
    # Required
    SEO_SETTINGS = SeoSettings.objects.last()
    FOOTER_SETTINGS = FooterSettings.objects.last()
    SOCIAL_SETTINGS = SocialSettings.objects.all()
    LOGO_SETTINGS = LogoSettings.objects.last()
    ONE_HEADER = OneHeader.objects.all()
    TWO_HEADER = TwoHeader.objects.all()
    RIGHT_BUTTON_SETTINGS = RightButtonSettings.objects.last()
    PHONE_EMAIL_SETTINGS = PhoneEmailSettings.objects.last()

    # Main
    SLAYDLAR = Slayd.objects.all()
    page_num = request.GET.get('page', 1)
    paginator = Paginator(SLAYDLAR, 9)

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    ctx = {
        # Required
        'SEO_SETTINGS': SEO_SETTINGS,
        'FOOTER_SETTINGS': FOOTER_SETTINGS,
        'SOCIAL_SETTINGS': SOCIAL_SETTINGS,
        'LOGO_SETTINGS': LOGO_SETTINGS,
        'ONE_HEADER': ONE_HEADER,
        'TWO_HEADER': TWO_HEADER,
        'RIGHT_BUTTON_SETTINGS': RIGHT_BUTTON_SETTINGS,
        'PHONE_EMAIL_SETTINGS': PHONE_EMAIL_SETTINGS,

        # Main
        'SLAYDLAR': page_obj,
        'page_num': page_num,

    }
    return render(request, 'courses/slayd.html', ctx)

def maruza_page(request):
    # Required
    SEO_SETTINGS = SeoSettings.objects.last()
    FOOTER_SETTINGS = FooterSettings.objects.last()
    SOCIAL_SETTINGS = SocialSettings.objects.all()
    LOGO_SETTINGS = LogoSettings.objects.last()
    ONE_HEADER = OneHeader.objects.all()
    TWO_HEADER = TwoHeader.objects.all()
    RIGHT_BUTTON_SETTINGS = RightButtonSettings.objects.last()
    PHONE_EMAIL_SETTINGS = PhoneEmailSettings.objects.last()

    # Main
    MARUZALAR = Maruza.objects.all()
    page_num = request.GET.get('page', 1)
    paginator = Paginator(MARUZALAR, 9)

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    ctx = {
        # Required
        'SEO_SETTINGS': SEO_SETTINGS,
        'FOOTER_SETTINGS': FOOTER_SETTINGS,
        'SOCIAL_SETTINGS': SOCIAL_SETTINGS,
        'LOGO_SETTINGS': LOGO_SETTINGS,
        'ONE_HEADER': ONE_HEADER,
        'TWO_HEADER': TWO_HEADER,
        'RIGHT_BUTTON_SETTINGS': RIGHT_BUTTON_SETTINGS,
        'PHONE_EMAIL_SETTINGS': PHONE_EMAIL_SETTINGS,

        # Main
        'MARUZALAR': page_obj,
        'page_num': page_num,

    }
    return render(request, 'courses/maruza.html', ctx)

def amaliy_page(request):
    # Required
    SEO_SETTINGS = SeoSettings.objects.last()
    FOOTER_SETTINGS = FooterSettings.objects.last()
    SOCIAL_SETTINGS = SocialSettings.objects.all()
    LOGO_SETTINGS = LogoSettings.objects.last()
    ONE_HEADER = OneHeader.objects.all()
    TWO_HEADER = TwoHeader.objects.all()
    RIGHT_BUTTON_SETTINGS = RightButtonSettings.objects.last()
    PHONE_EMAIL_SETTINGS = PhoneEmailSettings.objects.last()

    # Main
    AMALIYLAR = Amaliy.objects.all()
    page_num = request.GET.get('page', 1)
    paginator = Paginator(AMALIYLAR, 9)

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    ctx = {
        # Required
        'SEO_SETTINGS': SEO_SETTINGS,
        'FOOTER_SETTINGS': FOOTER_SETTINGS,
        'SOCIAL_SETTINGS': SOCIAL_SETTINGS,
        'LOGO_SETTINGS': LOGO_SETTINGS,
        'ONE_HEADER': ONE_HEADER,
        'TWO_HEADER': TWO_HEADER,
        'RIGHT_BUTTON_SETTINGS': RIGHT_BUTTON_SETTINGS,
        'PHONE_EMAIL_SETTINGS': PHONE_EMAIL_SETTINGS,

        # Main
        'AMALIYLAR': page_obj,
        'page_num': page_num,

    }
    return render(request, 'courses/amaliy.html', ctx)

def test_page(request):
    # Required
    SEO_SETTINGS = SeoSettings.objects.last()
    FOOTER_SETTINGS = FooterSettings.objects.last()
    SOCIAL_SETTINGS = SocialSettings.objects.all()
    LOGO_SETTINGS = LogoSettings.objects.last()
    ONE_HEADER = OneHeader.objects.all()
    TWO_HEADER = TwoHeader.objects.all()
    RIGHT_BUTTON_SETTINGS = RightButtonSettings.objects.last()
    PHONE_EMAIL_SETTINGS = PhoneEmailSettings.objects.last()

    # Main
    TESTLAR = Testlar.objects.all()
    page_num = request.GET.get('page', 1)
    paginator = Paginator(TESTLAR, 9)

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    ctx = {
        # Required
        'SEO_SETTINGS': SEO_SETTINGS,
        'FOOTER_SETTINGS': FOOTER_SETTINGS,
        'SOCIAL_SETTINGS': SOCIAL_SETTINGS,
        'LOGO_SETTINGS': LOGO_SETTINGS,
        'ONE_HEADER': ONE_HEADER,
        'TWO_HEADER': TWO_HEADER,
        'RIGHT_BUTTON_SETTINGS': RIGHT_BUTTON_SETTINGS,
        'PHONE_EMAIL_SETTINGS': PHONE_EMAIL_SETTINGS,

        # Main
        'TESTLAR': page_obj,
        'page_num': page_num,

    }
    return render(request, 'courses/test.html', ctx)