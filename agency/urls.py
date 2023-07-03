
from django.contrib import admin
from django.urls import path

from homes.views import list_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list_views)
]
