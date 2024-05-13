"""
URL configuration for introSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('Menu/', views.viewMenu, name="Menu"),
    path('CreateOrder/', views.create_order, name='CreateOrder'),
    path('EditOrder/', views.edit_order, name="EditOrder"),
    path('Cart/', views.viewCart, name='Cart'),
    path('Cart/<int:order_id>/', views.viewCart, name="Cart"),
    path('Checkout/', views.checkout, name="Checkout"),
    path('Reviews/', views.review, name="Review"),
    #path('post/<int:pk>/', views.post_detail, name='post_detail'),
   #path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    #path('post/new/', views.post_new, name='post_new'),
    #path('drafts/', views.post_draft_list, name='post_draft_list'),
    #path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    #path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    #path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    #path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
   # path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
