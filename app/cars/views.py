from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *

from cars.forms import ProdForm
from cars.models import *
from cars.repository import ChemClassRepository, ProdRepository


def index_page(request):
    """
    Возвращает список продукции, доступной для покупки
    """
    return render(request, '_template.html')


# Блок по работе с моделью EI
class EIList(ListView):
    model = EI
    template_name = 'ei/list.html'
    paginate_by = 10


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
    paginate_by = 10


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
    paginate_by = 10


class ProdView(DetailView):
    model = Prod
    template_name = 'prod/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProdView, self).get_context_data()
        myobject = self.object
        context['object'] = myobject
        connected = ChemClass.objects.filter(main_class=myobject.id_class.id)  # подсистемы авто: стеклоподъемник и ост.
        subs = []
        for con in connected:
            sub_con = ChemClass.objects.filter(main_class=con.id)  # компоненты подсистемы: ручка, кондесатор и т.д
            gubs = []
            for sub_c in sub_con:
                gubs.append({
                    'name': sub_c.name,
                    'short_name': sub_c.short_name,
                    'base_ei': sub_c.base_ei
                })
            subs.append(
                {
                    'name': con.name,
                    'short_name': con.short_name,
                    'base_ei': con.base_ei,
                    'components': gubs
                }
            )
        context['connected'] = subs
        # Then return
        return context


class ProdCreate(CreateView):
    model = Prod
    success_url = reverse_lazy('prod_list')
    template_name = 'prod/_form.html'
    form_class = ProdForm


class ProdUpdate(UpdateView):
    model = Prod
    fields = ['name', 'short_name', 'conf', 'id_class', 'type_prod']
    success_url = reverse_lazy('prod_list')
    template_name = 'prod/_form.html'


class ProdDelete(DeleteView):
    model = Prod
    success_url = reverse_lazy('prod_list')
    template_name = 'prod/delete.html'


def get_chem_children(request):
    """
    Возвращает потомков класса изделия
    """
    chem_class_id = request.GET.get('chem_class_id', None)
    products = ChemClassRepository.get_child(chem_class_id)
    classes = []
    for c_class in products:
        classes.append({
            'id': c_class.pk,
            'name': c_class.name,
        })
    data = {
        'classes': classes
    }
    return JsonResponse(data)


def get_chem_products(request):
    """
    Возвращает изделия класса
    """
    chem_class_id = request.GET.get('chem_class_id', None)
    products = ProdRepository.get_class_production(chem_class_id)
    classes = []
    for c_class in products:
        classes.append({
            'id': c_class.pk,
            'name': c_class.name,
        })
    data = {
        'classes': classes
    }
    return JsonResponse(data)
