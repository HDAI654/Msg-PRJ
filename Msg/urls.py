from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('APAS/', admin.site.urls),
    path('auth/', include("auth_.urls")),
    path('', include("Messenger.urls")),
]