"""thebakersystem URL Configuration

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
from thebakerorders import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('template/', views.customers, name="template"),
    path('', views.login,name='login'),
    path('go_back/', views.back_to_home,name='go_back'),
    path('additem/', views.additem, name="additem"),
    path('signup/', views.sign_up,name='signup'),
    path('status/', views.back_to_home,name='status'),
    path('order_request/', views.add_order,name='order_request'),
    path('logout/',views.logout, name="logout")
]
