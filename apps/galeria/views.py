from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from galeria.models import Veiculo, Marca, Foto
from galeria.forms import VeiculoForms, FotoForm
from usuarios.models import Favorito, User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    marcas = Marca.objects.filter().order_by('marca')
    return render(request,"index.html", {"marcas":marcas})

def estoque(request):
    '''Estoque com Paginação e Verificação de Favoritos'''
    veiculos = Veiculo.objects.filter(publicada=True)
    paginator = Paginator(veiculos, 8)
    page = request.GET.get('page')
    veiculos_por_page = paginator.get_page(page)
    marcas = Marca.objects.filter().order_by('marca')
    if request.user.is_authenticated:
        veiculos_favoritados = Favorito.objects.filter(user=request.user).values_list('item', flat=True)
        return render(request, 'estoque.html', {'cards': veiculos_por_page, 'veiculos_favoritados': veiculos_favoritados, "marcas":marcas})
    else:
        return render(request, 'estoque.html', {'cards': veiculos_por_page,  "marcas":marcas})

def produto(request, foto_id):
    '''Pagina de Produto e Verificação de Favorito'''
    veiculo = get_object_or_404(Veiculo, pk=foto_id)
    fotos = Foto.objects.filter(veiculo=veiculo).order_by('posicao')
    if request.user.is_authenticated:
        veiculos_favoritados = Favorito.objects.filter(user=request.user).values_list('item', flat=True)
        return render(request, "produto.html", {'veiculo': veiculo, 'fotos':fotos,'veiculos_favoritados': veiculos_favoritados })
    else:
        return render(request, "produto.html", {'veiculo': veiculo , 'fotos':fotos})

def buscar(request):
    '''Busca por Nome'''
    veiculos = Veiculo.objects.filter(publicada=True)
    paginator = Paginator(veiculos, 8)
    page = request.GET.get('page')
    veiculos_por_page = paginator.get_page(page)
    marcas = Marca.objects.filter()
    if "buscar" in request.GET:
        buscador = request.GET['buscar']
        if buscador:
            veiculos = Veiculo.objects.filter(nome__icontains=buscador)
            paginator = Paginator(veiculos, 8)
            veiculos_por_page = paginator.get_page(page)
        if request.user.is_authenticated:
            veiculos_favoritados = Favorito.objects.filter(user=request.user).values_list('item', flat=True)
            return render(request, 'estoque.html', {'cards': veiculos_por_page   , 'veiculos_favoritados': veiculos_favoritados,  "marcas":marcas})
        else:
            return render(request, 'estoque.html', {'cards': veiculos_por_page,  "marcas":marcas})
    return render(request,"estoque.html",{"cards":veiculos,  "marcas":marcas})

def filtro(request, tipo):
    '''Filtro de Veiculo + Marcas'''
    marcas = Marca.objects.filter(tipo=tipo)
    veiculos = Veiculo.objects.order_by("nome").filter(publicada=True, tipo=tipo)
    paginator = Paginator(veiculos, 8)
    page = request.GET.get('page')
    veiculos_por_page = paginator.get_page(page)
    if request.user.is_authenticated:
        veiculos_favoritados = Favorito.objects.filter(user=request.user).values_list('item', flat=True)
        return render(request, 'estoque.html', {'cards':veiculos_por_page, 'veiculos_favoritados': veiculos_favoritados, "marcas":marcas})
    return render(request,'estoque.html',{'cards':veiculos_por_page,  "marcas":marcas})

def filtroMarca(request, marca):
    '''Filtro por Marcas'''
    marcas = Marca.objects.filter()
    veiculos = Veiculo.objects.order_by("nome").filter(publicada=True, marca__marca=marca)
    paginator = Paginator(veiculos, 8)
    page = request.GET.get('page')
    veiculos_por_page = paginator.get_page(page)
    if request.user.is_authenticated:
        veiculos_favoritados = Favorito.objects.filter(user=request.user).values_list('item', flat=True)
        return render(request, 'estoque.html', {'cards':veiculos_por_page, 'veiculos_favoritados': veiculos_favoritados, "marcas":marcas})
    return render(request,'estoque.html',{'cards':veiculos_por_page,  "marcas":marcas})

@login_required(login_url='login')
def adicionar_veiculo(request):
    '''Anunciar Veiculo'''
    form = VeiculoForms()
    user_profile = request.user
    inputs = ['Ano', 'Km', 'Tipo', 'Portas', 'Motor', 'Cor', 'Cambio']
    if request.method == 'POST':
        form = VeiculoForms(request.POST, request.FILES)
        if form.is_valid(): 
            form = form.save(commit=False)
            form.user = user_profile  
            form.save()
            messages.success(request, 'Anúncio Criado!')
            return redirect('editar_veiculo', form.id)
    return render(request, 'adicionar_veiculo.html', {'form': form,'inputs': inputs,})

def editar_veiculo(request, foto_id):
    '''Editar Veiculo Anunciado e Fotos'''
    veiculo = get_object_or_404(Veiculo, id=foto_id)
    fotos = Foto.objects.filter(veiculo=veiculo).order_by('posicao')
    inputs = ['Ano', 'Km', 'Tipo', 'Portas', 'Motor', 'Cor', 'Cambio']
    forms = []
    for foto in fotos:
        formulario = FotoForm(instance=foto)
        forms.append({'form': formulario, 'foto': foto})
    if request.method == 'POST':
        form = VeiculoForms(request.POST, instance=veiculo)
        if form.is_valid(): 
            form.save()
            messages.success(request, 'Anúncio Editado!')
            return redirect('produto', foto_id)
    else:
        form = VeiculoForms(instance=veiculo)
    return render(request, 'editar_veiculo.html', {'form': form, 'forms': forms, 'fotos': fotos, 'foto_id': foto_id, 'inputs': inputs, 'veiculo':veiculo})

def deletar_veiculo(request, foto_id):
    veiculo = Veiculo.objects.get(id=foto_id)
    veiculo.delete()
    return redirect('estoque')

def adicionar_foto(request, veiculo_id):
    '''Adicionar Foto para o Veiculo'''
    veiculo = get_object_or_404(Veiculo, id=veiculo_id)
    if request.method == 'POST':
        form = FotoForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            foto = form.save(commit=False)
            foto.veiculo = veiculo  
            foto.save()
            messages.success(request, 'Foto Adicionada!')
            return redirect('editar_veiculo', veiculo_id)
    else:
        form = FotoForm()
    return render(request, 'adicionar_foto.html', {'form': form, 'veiculo': veiculo})

def editar_foto(request, foto_id):
    '''Editar ordem e alterar foto do veiculo'''
    foto = get_object_or_404(Foto, id=foto_id)
    if request.method == 'POST':
        form = FotoForm(request.POST, instance=foto)
        if form.is_valid():
            form.save()
            current_url = request.META.get('HTTP_REFERER', '/')
            messages.success(request, 'Foto Editada!')
            return redirect(current_url)
        
def deletar_foto(request, foto_id):
    foto = Foto.objects.get(id=foto_id)
    foto.delete()
    current_url = request.META.get('HTTP_REFERER', '/')
    messages.success(request, 'Foto Deletada!')
    return redirect(current_url)

