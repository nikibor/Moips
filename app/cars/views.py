from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from .models import ChemClass, EI, Prod


def index_page(request):
    """
    Возвращает список продукции, доступной для покупки
    """
    return render(request, '_template.html')


# Блок по работе с моделью EI
class EIList(ListView):
    model = EI
    template_name = 'ei/list.html'


class EIView(DetailView):
    model = EI
    template_name = 'ei/detail.html'


class EICreate(CreateView):
    model = EI
    fields = ['code', 'name', 'short_name']
    success_url = reverse_lazy('ei_list')
    template_name = 'ei/_form.html'


class EIUpdate(UpdateView):
    model = EI
    fields = ['code', 'name', 'short_name']
    success_url = reverse_lazy('ei_list')
    template_name = 'ei/_form.html'


class EIDelete(DeleteView):
    model = EI
    success_url = reverse_lazy('ei_list')
    template_name = 'ei/delete.html'


# Блок по работе с сущностью ChemClass
class ChemClassList(ListView):
    model = ChemClass
    template_name = 'сhemClass/list.html'


class ChemClassView(DetailView):
    model = ChemClass
    template_name = 'сhemClass/detail.html'


class ChemClassCreate(CreateView):
    model = ChemClass
    fields = ['name', 'short_name', 'base_ei', 'main_class']
    success_url = reverse_lazy('сhemClass_list')
    template_name = 'сhemClass/_form.html'


class ChemClassUpdate(UpdateView):
    model = ChemClass
    fields = ['name', 'short_name', 'base_ei', 'main_class']
    success_url = reverse_lazy('сhemClass_list')
    template_name = 'сhemClass/_form.html'


class ChemClassDelete(DeleteView):
    model = ChemClass
    success_url = reverse_lazy('сhemClass_list')
    template_name = 'сhemClass/delete.html'


# Блок по работе с сущностью Prod
class ProdList(ListView):
    model = Prod
    template_name = 'prod/list.html'


class ProdView(DetailView):
    model = Prod
    template_name = 'prod/detail.html'


class ProdCreate(CreateView):
    model = Prod
    fields = ['name', 'short_name', 'conf', 'id_class', 'type_prod']
    success_url = reverse_lazy('prod_list')
    template_name = 'prod/_form.html'


class ProdUpdate(UpdateView):
    model = Prod
    fields = ['name', 'short_name', 'conf', 'id_class', 'type_prod']
    success_url = reverse_lazy('prod_list')
    template_name = 'prod/_form.html'


class ProdDelete(DeleteView):
    model = Prod
    success_url = reverse_lazy('prod_list')
    template_name = 'prod/delete.html'
