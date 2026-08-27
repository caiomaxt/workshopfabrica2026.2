from django.shortcuts import render, redirect, get_object_or_404
from .forms import UsuarioForm
from .models import Usuario

def home(request):
    return render(request, 'app/home.html')

def register_view(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()  # Criptografa a senha e salva no banco automaticamente
            return redirect('home')  # Redireciona após salvar para evitar reenvio de form
    else:
        form = UsuarioForm()
        
    return render(request, 'app/register.html', {'form': form})

# View que estava faltando para a rota 'detail/<int:pk>/'
def detail_view(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    return render(request, 'app/detail.html', {'usuario': usuario})
