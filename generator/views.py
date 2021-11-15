from django.shortcuts import render
import random

# Create your views here.

# View for home page
def home(request):
    return render(request, 'generator/home.html')


# View for password page and function to generate password
def password(request):

    gen_password = ''

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%&'))

    length = int(request.GET.get('length'))

    for i in range(length):
        gen_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': gen_password})

# View for about page
def about(request):
    return render(request, 'generator/about.html')
