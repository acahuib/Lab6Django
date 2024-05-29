from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestion_notas/', include('gestion_notas.urls')),
    path('', RedirectView.as_view(url='/gestion_notas/')),  # Redirige la URL raíz a la aplicación gestion_notas
]

