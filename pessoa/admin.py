from django.contrib import admin
from .models import Pessoa, Contato

@admin.action(description='Ativar Todos')
def ativar_todos(modelAdmin, request, queryset):
    queryset.update(ativa=True)

@admin.action(description='Desativar Todos')
def desativar_todos(modelAdmin, request, queryset):
    queryset.update(ativa=False)
    
class pessoaAdmin(admin.ModelAdmin):
    list_display = [
        'nome_completo',
        'data_nascimento',
        'ativa'
    ]
    list_filter = [
        'ativa'
    ]
    search_fields = [
        'nome_completo',
        'data_nascimento'
    ]
    actions = [
        ativar_todos,
        desativar_todos
    ]

admin.site.register(Pessoa, pessoaAdmin)
admin.site.register(Contato)