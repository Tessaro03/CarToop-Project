from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from usuarios.models import Favorito
from galeria.models import Veiculo

from django.contrib import messages

def login(request):
    form = LoginForms()
    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()
        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )
        try:
            if usuario is not None:
                auth.login(request, usuario)
                return redirect('index')
        except:
            return redirect('login')
        else:
            messages.error(request, 'Erro ao efetuar login')
            return redirect('login')

    return render(request, 'usuarios/login.html', {'form': form})


def cadastro(request):
    form = CadastroForms()
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        if form.is_valid():  # Verificar se o formulário é válido
            if form.cleaned_data['senha_1'] != form.cleaned_data['senha_2']:
                messages.error(request, 'Senhas Diferentes!')
                return redirect('cadastro')
            
            nome = form.cleaned_data['nome_cadastro']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha_2']
            nome_completo = form.cleaned_data['nome']

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Nome de Login já Existe!')
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email= email,
                password=senha,
                first_name=nome_completo,
            )
            usuario.save()
            
            usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
            )
            if usuario is not None:
                auth.login(request, usuario)
                return redirect('index')
            
            messages.success(request, 'Cadastro feito com Sucesso!')
            
            return redirect("login")
    return render(request,'usuarios/cadastro.html',{'form':form})



def logout(request):
    auth.logout(request)
    messages.success(request,'Logout Feito!')
    return redirect('login')

@login_required(login_url='login')
def perfil(request):
    '''Perfil, é passsado veiculos Favoritados e Anunciados'''
    user = request.user
    favoritos = Favorito.objects.filter(user=user)
    veiculos_favoritados = [favorito.item for favorito in favoritos]
    anunciados = Veiculo.objects.filter(user=user)
    return render(request, 'usuarios/perfil.html',  {'veiculos_favoritados': veiculos_favoritados, 'usuario':user,'anunciados': anunciados })

def favoritar(request, item_id):
    '''Favoritar Veiculo'''
    item = get_object_or_404(Veiculo, pk=item_id)
    Favorito.objects.get_or_create(user=request.user, item=item)
    current_url = request.META.get('HTTP_REFERER')
    return redirect(current_url)

def desfavoritar(request, item_id):
    item = get_object_or_404(Veiculo, pk=item_id)
    Favorito.objects.filter(user=request.user, item=item).delete()
    current_url = request.META.get('HTTP_REFERER')
    return redirect(current_url)