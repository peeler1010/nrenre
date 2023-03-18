from django.contrib import admin
from django.urls import path
from . views import home, list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('list/', list, name='list')
]
