from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            print("Валидация прошла")

            return redirect('hello')
        else:


            visible='visible'
            # if form.cleaned_data.get('password1')=="":
            #     print("Пустой парол1")
            # if form.cleaned_data.get('password2')=="":
            #     print("Пустой парол2")
    else:
        visible='no_visible'
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form,'error': visible})


@login_required
def profile(request):
    return render(request, 'profile.html')
