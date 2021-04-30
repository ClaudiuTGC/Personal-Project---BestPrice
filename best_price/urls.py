"""best_price URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from users import views as users_views
from home import views as home_views
from products import views as products_views
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from wishlist import views as list_views
from comments import views as com_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.home_page),
    path('home/', home_views.home_page, name='home'),
    path('register/', users_views.register_page, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'templates/users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'templates/users/logout.html'), name='logout'),
    path('products/<str:id>/', products_views.products_page, name='products'),
    path('fav/<int:id>/', list_views.list_add, name='list_add'),
    path('wishlist/', list_views.wishlist_page, name='wishlist'),
    path('product/<int:id>/', com_views.comments_view, name='product'),
]
