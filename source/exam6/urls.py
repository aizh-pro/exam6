"""exam6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from webapp.views import record_create_view, index_view, record_update_view, record_delete_view, search_result_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('records/add/', record_create_view, name='record_create'),
    path('record/<int:pk>/update/', record_update_view, name='record_update'),
    path('record/<int:pk>/delete/', record_delete_view, name='record_delete'),
    path('search/result/', search_result_view, name='search_result')
]
