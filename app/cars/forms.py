from django import forms

from cars.models import Prod


class ProdForm(forms.ModelForm):
    #     name = forms.CharField(label='Полное название изделия')
    #     short_name = forms.CharField(label='Обозначение изделия')
    #     conf = forms.IntegerField(min_value=1, label='Терминальный класс изделия')
    #     id_class = forms.ChoiceField(label='Класс изделия', widget=forms.Select())
    #     type_prod = forms.ChoiceField(label='Родительское изделие', widget=forms.Select(), choices=())

    class Meta:
        model = Prod
        fields = ('name', 'short_name', 'conf', 'id_class', 'type_prod')
