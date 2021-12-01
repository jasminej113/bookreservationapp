"""bookreservation URL Configuration

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
from reservation import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', views.dashboard, name='dashboard'),
	path('studentdetails/', views.studentdata, name='studentdetails'),
	path('bookdetails/', views.bookdata, name='bookdetails'),
	path('bookreservation/', views.reserve, name='bookreservation'),
	path('login/', LoginView.as_view(template_name='reservation/login.html'), name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),
	path('savereservation/', views.savereservation, name='savereservation'),
	# override login from django 
	
]
