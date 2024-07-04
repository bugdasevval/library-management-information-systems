"""
URL configuration for lims_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home),
    path('home', home),
    path('readers', readers_tab, name='readers_tab'),
    path('books', books),
    path('save', save_student),
    path('returns', returns),
    path('save_loan/', save_loan, name='save_loan'),
    path('kayit', kayit, name='kayit'),
    path('save_student/', save_student, name='save_student'),
    path('ceza/', ceza_view, name='ceza'),
    path('search_reader/', search_reader, name='search_reader'),
    path('edit_reader/<int:id>/', edit_reader, name='edit_reader'),
    path('delete_reader/<int:id>/', delete_reader, name='delete_reader'),
    path('delete_loan/<int:id>/', delete_loan, name='delete_loan'),
    path('edit_loan/<int:id>/', edit_loan, name='edit_loan'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

