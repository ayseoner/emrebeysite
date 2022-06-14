"""emrebeysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from django.views.static import serve
from django.shortcuts import redirect
from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps.views import sitemap
from django.contrib.flatpages.sitemaps import FlatPageSitemap
from django.views.generic import TemplateView


from pages.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('hakkimizda/', firmaklinigihakkinda, name='hakkimizde'),
    path('tarihce/', tarihce, name='tarihce'),
    path('iletisim/', iletisim, name='iletisim'),
    path('hizmetlerimiz/', hizmetlerimiz, name='hizmetlerimiz'),

    path('hizmetlerimiz/ar-ge-hizmetleri/', ar_ge_hizmetleri, name='ar-ge-hizmetleri'),
    path('hizmetlerimiz/destek-hizmetleri/', destek_hizmetleri, name='destek_hizmetleri'),
    path('hizmetlerimiz/genel-hibe-ve-tesvik-danismanligi/', genel_hibe_ve_tesvik_danismanligi, name='genel_hibe_ve_tesvik_danismanligi'),
    path('hizmetlerimiz/proje-yazim-ve-yönetimi-hizmetleri/', proje_yazim_ve_yönetimi_hizmetleri, name='proje_yazim_ve_yönetimi_hizmetleri'),
    path('hizmetlerimiz/sirket-degerleme/', sirket_degerleme, name='sirket_degerleme'),
    path('hizmetlerimiz/yatirim-ve-tesvik-danismanligi/', yatirim_ve_tesvik_tanismanligi, name='sirket_degerleme'),
    path('hizmetlerimiz/vergi-ve-sigorta-danismanligi/', vergi_ve_sigorta_danismanligi, name='ar-ge-vergi_ve_sigorta_hizmetleri'),

    path('hizmetlerimiz/ar-ge-hizmetleri/check-up-hizmeti/', check_up_hizmeti, name='check_up_hizmeti'),
    path('hizmetlerimiz/ar-ge-hizmetleri/periyodik-ar-ge-danismanligi/', periyodik_arge_danismanligi, name='periyodik_arge_danismanligi'),
    path('hizmetlerimiz/ar-ge-hizmetleri/ar-ge-muhasebesi-danismanlik-hizmeti/', ar_ge_muhasebesi_danismanlik_hizmeti, name='ar_ge_muhasebesi_danismanlik_hizmeti'),
    path('hizmetlerimiz/ar-ge-hizmetleri/portal-hizmetleri/', portal_hizmetleri, name='portal_hizmetleri'),

    path('iletisimegec/', bizimleiletisimegecin, name='iletisimegec')


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
