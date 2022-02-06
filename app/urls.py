from django.urls import path
from . import views

urlpatterns = [
    path('brands/register', views.index),
    path('brands/login', views.brand_login),
    path('brands/dashboard', views.brands_dash),
    path('talent/register',views.index_two),
    path('talent/login', views.talent_login),
    path('talent/dashboard', views.talent_dash),
    path('brands/new', views.add_new),
    path('brands/create', views.create_job),
    path('brands/favorite/<int:talent_id>', views.favorite),
    path('brands/login', views.logout),
]   
