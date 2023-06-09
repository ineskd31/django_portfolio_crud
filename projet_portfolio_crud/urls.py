"""
URL configuration for projet_portfolio_crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from app_home.views import *
from app_back_home.views import *
from app_about.views import *
from app_skills.views import *
from app_service.views import *
from app_testimonials.views import *
from app_portfolio.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='homefront'),
    
    path('backhome/', backhome, name="homeback" ),
    path('edit/<int:id>', edit, name='edit'),
    
    path('skillsInfo/', skillsInfo, name='skillsInfo'),
    path('editSkills/<int:id>', skillsEdit, name='skillsEdit'),
    path('info/destroy/<int:id>', delete),
    path('ajouter/', ajouter, name="ajouter"),
    
    path('infoService/', infoService, name='infoService'),
    path('infoService/destroy/<int:id>', deleteService),
    path('addService/', addService, name='addService'),
    path('editService/<int:id>', editService, name='editService'),

    path('infoTesti/', infoTesti, name='infoTesti'),
    path('addTesti/', addTesti, name='addTesti'),
    path('editTesti/<int:id>', editTesti, name='editTesti'),
    path('infoTesti/destroy/<int:id>', deleteTesti),
    
    path('infoPort/', infoPort, name='infoPort'),
    path('addFilter/', addPortFilter, name='addPortFilter'),
    path('addImage/', addPortImage, name='addPortImage'),
    path('deletePortFilter/destroy/<int:id>', deletePortFilter),
    path('deletePortImage/destroy/<int:id>', deletePortImage),
    
    
]
