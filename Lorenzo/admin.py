from django.contrib import admin
from .models import MinhaHistoria, MeusDados, MeuPortifolio, Formacao, Experiencias, Cursos, Infos

# Register your models here.
admin.site.register(MinhaHistoria)
admin.site.register(MeusDados)
admin.site.register(MeuPortifolio)
admin.site.register(Formacao)
admin.site.register(Experiencias)
admin.site.register(Cursos)
admin.site.register(Infos)