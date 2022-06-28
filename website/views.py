from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required 

def Cadastro (request):
    if request.method == 'GET':
        return render(request, ('website/cadastro.html'))
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        #Verifica se há um usuário já cadastrado com esse nome.
        user = User.objects.filter(username = username).first()
        
        if user:
            return HttpResponse('Usuário já existe')
        
        #Cria um usuário novo e cadastra no BD
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
            return render(request, 'website/home.html')
        else:
            return HttpResponse('Username ou senha inválidos')

@login_required(login_url="/auth/login/")
def Home(request):
    return render(request, 'website/home.html')
    
    


        
    
