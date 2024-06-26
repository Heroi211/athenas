"""
URL configuration for api project.

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

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from person.api.viewsets import PersonViewSet
from person.views import calcular_peso_ideal

router = routers.DefaultRouter()
router.register(r'person', PersonViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('person', PersonViewSet.as_view({'get': 'list', 'post': 'create'}), name='person-list'),
    path('person/<int:pk>', PersonViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'}), name='person-detail'),
    path('person/pesoIdeal/<int:pk>', calcular_peso_ideal, name='person-peso-ideal')
] + router.urls
