
from django.urls import path
from inicioapp import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    
    path('',views.inicio, name= 'index'),
    path('contacto/',views.contacto,name= 'contacto'),
]
urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)