from django.contrib import admin
from django.urls import path, include
from core import views
from django.http import JsonResponse


def chess_tip(request):
    return JsonResponse({'tip': 'Control the center of the board!'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),       # homepage
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('tip/', chess_tip, name='tip'),
   path('logout/', views.logout_view, name='logout'),
path('accounts/', include('django.contrib.auth.urls')),

]

