from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

urlpatterns = [
    # Home page FIRST
    path('', home, name='home'),

    # Admin panel
    path('admin/', admin.site.urls),

    # Student login & dashboard
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),

    # Other apps
    path('attendance/', include('attendance.urls')),
    path('fees/', include('fees.urls')),
    path('discipline/', include('discipline.urls')),
    path('hostel/', include('hostel.urls')),
    path('notices/', include('notices.urls')),
]
