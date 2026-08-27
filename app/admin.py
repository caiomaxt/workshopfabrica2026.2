from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'age', 'phone', 'date_joined')
    search_fields = ('username', 'phone')