from django.urls import path
from usuarios.views import *

urlpatterns = [
    path("login",login, name='login'),
    path('cadastrar-se', cadastro, name='cadastro'),
    path('logout', logout, name='logout'),
    path('perfil',perfil,name='perfil'),
    path('favoritar/<int:item_id>/', favoritar, name='favoritar'),
    path('desfavoritar/<int:item_id>/', desfavoritar, name='desfavoritar'),
]