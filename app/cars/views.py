from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from .models import ChemClass, EI


def index_page(request):
    """
    Возвращает список продукции, доступной для покупки
    """
    return render(request, '_template.html')


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
