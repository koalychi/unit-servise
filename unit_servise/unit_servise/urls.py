from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('unit/', include("unit.urls")),
    path('admin/', admin.site.urls),
]
