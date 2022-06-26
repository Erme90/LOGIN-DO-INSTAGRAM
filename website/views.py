from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

def Cadastro (request):
    if request.method == 'GET':
        return render(request, ('website/cadastro.html'))
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username = username).first()
        
        if user:
            return HttpResponse('Usuário já existe')
        
        user = User.objects.create_user(username = username, email=email, password = senha)
        user.save()

        return HttpResponse('Usuário cadastrado com sucesso!')


def Login (request):
    if request.method == 'GET':
        return render(request, ('website/login.html'))
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        user = authenticate(username = username, password = senha)

        if user:
            login(request, user)
            return HttpResponse ('AUTENTICADO!')
        else:
            return HttpResponse('Username ou senha inválidos')


def Home(request):
    if request.user.is_authenticated():
        return HttpResponse ('AUTENTICADO!')
    else:
        return HttpResponse('Você não está logado')


    


        
    
