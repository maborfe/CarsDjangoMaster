from Car import views 
from django.contrib import admin
from django.urls import path

# Adicionados estes imports para informar ao django e ao seu gestor de urls principal que existe tratamento de media
# para este projeto, através do comando de arquivos staticos (static(.........)) concatenado ao urlpatterns
# As configurações de media url e media root estao no settings do projeto.
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', views.car_home, name='car_home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)