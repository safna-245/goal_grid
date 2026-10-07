"""
URL configuration for goal_grid project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path,include
from kickora import views
from playslot.views import BookingsListCreateView
from playslot.views import BookingsRetrieveUpdateDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-register/',views.AdminRegisterView.as_view()),

    path('turfs/',views.TurfListCreateView.as_view()),
    path('turfs/<int:pk>/',views.TurfRetrieveUpdateDeleteView.as_view()),

    path('bookings/',BookingsListCreateView.as_view()),
    path('bookings/<int:pk>/',BookingsRetrieveUpdateDeleteView.as_view()),

    path('v2/bookings/',include("playslot_v2.urls")),
    
]
