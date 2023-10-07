from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # Import settings module
from django.conf.urls.static import static  # Import static function

import products.views
import accounts
import products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', products.views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
]

# Serve media and static files during development

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
