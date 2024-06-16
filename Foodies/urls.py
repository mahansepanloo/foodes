from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls',namespace='home')),
    path('accounts/', include('accounts.urls',namespace='accounts')),
    path('orders/',include("orders.urls",namespace='order'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

