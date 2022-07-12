from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

                                                      #PARA ENTENDER LINHA A LINHA:
def Cadastro (request):                                  #função Cadastro para a view.

    if request.method == 'POST':                      #Se o request for um metodo POST (ou seja, de envio de informações)
        form_usuario = UserCreationForm(request.POST) #esta variavel chama o modulo "UserCreationForm" com a instancia do "IF"
        if form_usuario.is_valid():                   #Se os dados informados forem válidos
            form_usuario.save()                       #Então o usuário é salvo()
            return redirect('/auth/login')            #E é redirecionado para a página de login
    else:                                             #Se não
        form_usuario = UserCreationForm()             #Ele abre um novo formulário para o usuário cadastrar-se
    return render(request,'website/cadastro.html', {'form_usuario': form_usuario})#E envia o usuário para a página de cadastro.
    
    
def Login (request):                                                #nome da função
                                                                    ######################################################################################
    if request.method == 'GET':                                     # Se o metodo de requisição for igual a "GET" (buscar a página pela URL)
        return render(request, ('website/login.html'))              # Retorna uma renderização do template de 'login'
    else:                                                           # Se não
        username = request.POST.get('username')                     # A variavel 'username' recebe uma requisição 'POST' para buscar o username cadastrado
        senha = request.POST.get('senha')                           # A variavel 'password' recebe uma requisição 'POST' para buscar a senha cadastrado
        user = authenticate(username = username, password = senha)  # A variavel 'User' recebe uma autenticação do 'username' e do 'password'
                                                                    #######################################################################################
        if user:                                                    # Se a varival 'User' retorna uma informação 'True' (verdadeira. Ou seja, se existe este usuário com esta senha)
            return render(request, 'website/home.html')             # Retorna uma renderização do template 'home'
        else:                                                       # Se não
            return HttpResponse('SENHA OU USUÁRIO INVÁLIDO')        # Retorna uma mensagem de erro "usuário ou senha inválida"
                                                                    ######################################################################################
@login_required(login_url="/auth/login/")                           # Um decorator de "login_required", se a autenticação for OK então ele envia para a pagina 'home'
                                                                    #OBS.: Este decorator, é que faz com que a página só seja acessada, se for por meio de login (escrever na url não funciona)
def Home(request):
    return render(request, 'website/home.html')
    
    


        
    
