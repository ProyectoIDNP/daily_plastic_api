"""daily_plastic_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

from apps.users.views import Login, Logout
from apps.users_plastics.views import ReportCategoryUnit, ReportCategoryWeight, ReportPresentationUnit, ReportPresentationWeight

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/login/', Login.as_view(), name = 'login'),
    path('api/auth/logout/', Logout.as_view(), name = 'logout'),
    path('api/report/categories/unit/', ReportCategoryUnit.as_view(), name = 'ReportCategoryUnit'),
    path('api/report/categories/weight/', ReportCategoryWeight.as_view(), name = 'ReportCategoryWeight'),
    path('api/report/presentations/unit/', ReportPresentationUnit.as_view(), name = 'ReportPresentationUnit'),
    path('api/report/presentations/weight/', ReportPresentationWeight.as_view(), name = 'ReportPresentationWeight'),
    path('api/users/plastics/', include('apps.users_plastics.urls')),
    path('api/plastics/', include('apps.plastics.urls')),
    path('api/users/', include('apps.users.urls')),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]