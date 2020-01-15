
from django.contrib import admin
from django.urls import path, include
import hello.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('logout', views.logout, name="logout"),
    path('reserve', views.reserve, name="reserve"),
    path('diary', views.diary, name="diary"),
    path('accounts/', include('allauth.urls')),
    path('oauth/', views.oauth, name="oauth"),
    path('verification', views.verification, name="verification"),
]
