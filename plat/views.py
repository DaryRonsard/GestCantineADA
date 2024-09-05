from django.shortcuts import render, redirect, get_object_or_404
from .forms import PlatForms
from .models import PlatModel


# Create your views here.
def index(request):
    list_plat = PlatModel.objects.all()
    context = {'list_plat': list_plat}
    return render(request,'plat/listplat.html', context)


def create_plat(request):
    if request.method == 'POST':
        form = PlatForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plat_list')
    else:
        form = PlatForms()
    return render(request, 'plat/ajoutplat.html', {'form': form})


def modify_plat(request, id):
    plat = get_object_or_404(PlatModel, id=id)
    if request.method == 'POST':
        form = PlatForms(request.POST, instance=plat)
        if form.is_valid():
            form.save()
            return redirect('app_plat:index')
    else:
        form = PlatForms(instance=plat)
    return render(request, 'plat/updateplat.html', {'form': form})


def delete_plat(request, id):
    plat = get_object_or_404(PlatModel, id=id)
    if request.method == 'POST':
        plat.delete()
        return redirect('app_plat:index')
    return render(request, 'plat/deleteplat.html', {'plat': plat})