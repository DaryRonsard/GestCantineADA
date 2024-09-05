from django.urls import path
from plat.views import index, create_plat, modify_plat, delete_plat

app_name = 'app_plat'
urlpatterns = [
    path('', index, name='index'),
    path('creat_plat/', create_plat, name='creat_plat'),
    path('modify_plat/', modify_plat, name='modify_plat'),
    path('delete_plat/', delete_plat, name='delete_plat'),
]
