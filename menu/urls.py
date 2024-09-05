from django.urls import path
from menu import views
from menu.views import index, create_menu, modify_menu, delete_menu, list_menu

app_name = 'app_menu'
urlpatterns = [
    path('', index, name='dashboard'),
    path('list_menu/', list_menu, name='list-menu'),
    path('crate_menu/', create_menu, name='create-menu'),
    path('modify_menu/', modify_menu, name='modify-menu'),
    path('delete_menu/', delete_menu, name='delete-menu'),
]