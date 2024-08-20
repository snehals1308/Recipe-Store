from django.shortcuts import render , redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'home.html')

@login_required(login_url='/login/')
def recipe(request):

    if request.method == "POST":

        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_desc = data.get('recipe_desc')
        recipe_image = request.FILES.get('recipe_image')
        print(f"The recipe name is : {recipe_name}")
        print(f"The recipe description is : {recipe_desc}")
        print(f"The recipe image is : {recipe_image}")

        # if we want add this in database then,

        Recipe.objects.create(
            recipe_name = recipe_name,
            recipe_image = recipe_image,
            recipe_desc = recipe_desc,
        )
        
        return redirect('/recipe/')
    
    queryset = Recipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))

    context = {"recipe":queryset}
    return render(request,'recipe.html',context)

@login_required(login_url='/login/')
def recipe_delete(request,id):

    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/recipe/')

@login_required(login_url='/login/')
def recipe_update(request,id):
    queryset = Recipe.objects.get(id = id)

    if request.method == "POST":
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_desc = data.get('recipe_desc')
        recipe_image = request.FILES.get('recipe_image')

        queryset.recipe_name = recipe_name
        queryset.recipe_desc = recipe_desc
        if recipe_image:
            queryset.recipe_image = recipe_image

        queryset.save()
        return redirect('/recipe/')
    context = {'recipes':queryset}
    return render(request,'recipe_update.html',context)

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        if not User.objects.filter(username = username).exists():
            messages.info(request, "This username is not exists please register")
            return redirect('/login/')
        
        user = authenticate(username=username,password=password)

        if user is None:
            messages.info(request, "Invalid Password")
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/recipe/')
        


    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')


def register(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        check = User.objects.filter(username = username)

        if check.exists():
            messages.info(request, "This username is already exists please login")
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )
        user.set_password(password)
        user.save()

        messages.info(request, "Account Created Successfully")

        return redirect('/register/')

    return render(request,'register.html')