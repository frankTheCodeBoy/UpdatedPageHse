"""
URL configuration for tango_rango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, reverse, include
from django.conf import settings
from django.conf.urls.static import static
from registration.backends.simple.views import RegistrationView

class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return reverse('rango_app:register_profile')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rango_app.urls')),
    path(
        'accounts/register/', 
        MyRegistrationView.as_view(),
        name='registration_register'
        ),

    path('accounts/', include('registration.backends.simple.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
