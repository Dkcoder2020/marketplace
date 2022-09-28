from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home_page.urls')),
    path('user/',include('user_application.urls')),
    path('marketapp/',include('market_app.urls')),
    path('navbarapp/',include('navbar_application.urls')),

]
