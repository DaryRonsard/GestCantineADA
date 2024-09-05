from django.shortcuts import render, redirect, get_object_or_404
from .forms import MenuForm
from .models import MenuModels


# Create your views here.

def index(request):
    return render(request, 'menu/dashboard.html')


def list_menu(request):
    menus = MenuModels.objects.all()
    context = {'menus': menus}
    return render(request, 'menu/listmenu', context)


def create_menu(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_menu:index')
    else:
        form = MenuForm()
    return render(request, 'menu/createmenu.html', {'form': form})


def modify_menu(request, id):
    menu = get_object_or_404(MenuModels, id=id)
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            return redirect('app_menu:index')
    else:
        form = MenuForm(instance=menu)
    return render(request, 'menu/updatemenu.html', {'form': form})


def delete_menu(request, id):
    menu = get_object_or_404(MenuModels, id=id)
    if request.method == 'POST':
        menu.delete()
        return redirect('app_menu:index')
    return render(request, 'menu/deletemenu.html', {'menu': menu})
