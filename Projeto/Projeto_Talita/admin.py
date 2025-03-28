from django.contrib import admin
from .models import Usuario
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class UsuarioAdmin(UserAdmin):
    list_display = ('username', 'cpf', 'email', 'telefone', 'endereco')

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields':('telefone', 'cpf', 'endereco')}),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields':('telefone', 'cpf', 'endereco')}),
    )

admin.site.register(Usuario, UsuarioAdmin)