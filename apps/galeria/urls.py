from django.urls import path
from galeria.views import *

urlpatterns = [
    path("",index, name='index'),
    path('estoque', estoque, name='estoque'),
    path('produto/<int:foto_id>', produto,name='produto'),
    path('buscar',buscar,name='buscar'),
    path('filtro/<str:tipo>',filtro, name='filtro'),
    path('marca/<str:marca>',filtroMarca, name='filtroMarca'),

    path('adicionar-veiculo', adicionar_veiculo, name='adicionar_veiculo'),
    path('editar-veiculo/<int:foto_id>',editar_veiculo,name='editar_veiculo'),
    path('deletar-veiculo/<int:foto_id>',deletar_veiculo,name='deletar_veiculo'),

    path('adicionar-foto/<int:veiculo_id>', adicionar_foto, name='adicionar_foto'),
    path('editar-foto/<int:foto_id>',editar_foto,name='editar_foto'),
    path('deletar-foto/<int:foto_id>',deletar_foto,name='deletar_foto'),
]