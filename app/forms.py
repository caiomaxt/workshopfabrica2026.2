from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from .forms import UsuarioForm

def home(request):
    return render(request, 'app/home.html')

# Create your views here.
def register_view(request):
    if request.method == 'GET':
        form = UsuarioForm()
        return render(request, 'app/register.html', {'form': form})
    
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.password = make_password(usuario.password)
            usuario.save()
            request.status_code = 201

    else:
        form = UsuarioForm()

    return render(request, 'app/home.html', {'form': form})
