from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Django Admin Site
    path('admin/', admin.site.urls),

    # Main Site
    path('', include('BlueSkyMainApp.urls'))
]
