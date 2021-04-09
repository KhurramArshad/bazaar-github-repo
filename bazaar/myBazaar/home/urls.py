
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('<str:item>/<int:id>/', views.cat_items),
    path('<str:item>/', views.cat_items_detail, name='item_detail')
]