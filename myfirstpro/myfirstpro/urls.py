"""myfirstpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from myfirstapp import views


urlpatterns = [
     path('admin/', admin.site.urls),
     path('myfirstapp/', include('myfirstapp.urls')),
     path('myfirstapp/upload_record/', views.upload_record, name='upload_record'),
     path('myfirstapp/record_list/', views.record_list, name='record_list'),
     path('myfirstapp/class_record_list/', views.RecordListView.as_view(), name='class_record_list'),
     path('myfirstapp/record/<int:pk>/', views.RecordDetailView.as_view(), name='class_record_detail'),
     path('myfirstapp/class_record_update/<int:pk>/', views.RecordUpdateView.as_view(), name='class_record_update'),
     path('myfirstapp/class_record_delete/<int:pk>/', views.RecordDeleteView.as_view(), name='class_record_delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

