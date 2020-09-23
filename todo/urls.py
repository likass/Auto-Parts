from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('list.urls')),
                  path('', RedirectView.as_view(url='index/')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
