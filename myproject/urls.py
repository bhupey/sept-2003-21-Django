
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crud.urls')),
    path('', include('myapp.urls')),
    path('forms', include("temp_forms.urls")),
    path('inherit/', include('temp_inheritance.urls')),
    path('sr/',include('static_render.urls'))
    
]
