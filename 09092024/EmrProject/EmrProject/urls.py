"""
URL configuration for EmrProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from PatientApp import views
urlpatterns = [

    path('', view=views.list_of_patients, name='list_of_patients'),
    path('patients/', view=views.list_of_patients, name='list_of_patients'),
    path('patients/create/', view=views.create_patient, name='create_patient'),
    path('patients/edit/<id>/', view=views.edit_patient, name='edit_patient'),
    path('patients/delete/<id>/', view=views.delete_patient, name='delete_patient'),
    path('admin/', admin.site.urls),
]
