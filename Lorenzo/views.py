from django.shortcuts import render
from .models import MinhaHistoria, MeusDados, MeuPortifolio, Cursos, Formacao, Experiencias, Infos
from django.views.generic import TemplateView, ListView, DetailView
from datetime import datetime
# Create your views here.

class Homepage(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        data_nascimento = datetime(year=1998, month=4, day=6)
        data_inicial = datetime(year=2023, month=6, day=1)
        data_atual = datetime.now()

        meses_passados = (data_atual.year - data_inicial.year) * 12 + data_atual.month - data_inicial.month

        idade = data_atual.year - data_nascimento.year - ((data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day))

        context['meses_passados'] = meses_passados
        context['idade'] = idade
        return context


class Minhahistoria(DetailView):
    template_name = 'minhahistoria.html'
    model = MinhaHistoria

class Meusdados(DetailView):
    template_name = 'meusdados.html'
    model = MeusDados
    context_object_name = 'meusdados'

    def get_context_data(self, **kwargs):
        context = super(Meusdados, self).get_context_data(**kwargs)
        informacoes = Infos.objects.filter(nome=self.object)

        niveis = [info.nivel for info in informacoes]
        infos = [info.info for info in informacoes]

        context['niveis'] = niveis
        context['infos'] = infos
        return context

class Meuportifolio(ListView):
    template_name = 'meuportifolio.html'
    model = MeuPortifolio
    context_object_name = 'meuportifolio'