from django.contrib import admin
from django.urls import path
from studentorg import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.HomePageView.as_view(), name='home'),

    path(
        'organizations/',
        views.OrganizationListView.as_view(),
        name='organizations'
    ),

    path(
        'organizations/<int:pk>/',
        views.OrganizationDetailView.as_view(),
        name='organization_detail'
    ),
]