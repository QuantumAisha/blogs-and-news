"""
URL configuration for backend project.

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
from backend import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
     # User Profile CRUD Paths
    path('create_user_profile/', views.create_user_profile, name='create_user_profile'),
    path('read_user_profile/<str:username>/', views.read_user_profile, name='read_user_profile'),
    path('update_user_profile/<str:username>/', views.update_user_profile, name='update_user_profile'),
    path('delete_user_profile/<str:username>/', views.delete_user_profile, name='delete_user_profile'),
    path('user_profile_list/', views.user_profile_list, name='user_profile_list'),

     # User registration and login paths (if applicable)
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    
    # Article paths
    path('articles/', views.article_list),
    path('articles/<int:id>',views.article_detail),
    path('articles/category/<int:category_id>/',views.articles_by_category),
    path('articles/search/',views.search_articles, name='search-articles'),
    path('articles/published/', views.published_articles,name='published-articles'),
    path('articles/<int:article_id>/views/', views.view_article, name='view-article'),
    path('articles/share/<int:article_id>/', views.share_article, name='share-article'),
    # Category paths
    path('categories/', views.category_list),
    path('categories/<int:id>', views.category_detail)
]


urlpatterns = format_suffix_patterns(urlpatterns)