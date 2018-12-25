from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index_page, name='Index'),

    path('ei/', views.EIList.as_view(), name='ei_list'),
    path('ei/view/<int:pk>', views.EIView.as_view(), name='ei_view'),
    path('ei/new', views.EICreate.as_view(), name='ei_new'),
    path('ei/view/<int:pk>', views.EIView.as_view(), name='ei_view'),
    path('ei/edit/<int:pk>', views.EIUpdate.as_view(), name='ei_edit'),
    path('ei/delete/<int:pk>', views.EIDelete.as_view(), name='ei_delete'),

    path('сhemClass/', views.ChemClassList.as_view(), name='сhemClass_list'),
    path('сhemClass/view/<int:pk>', views.ChemClassView.as_view(), name='сhemClass_view'),
    path('сhemClass/new', views.ChemClassCreate.as_view(), name='сhemClass_new'),
    path('сhemClass/view/<int:pk>', views.ChemClassView.as_view(), name='сhemClass_view'),
    path('сhemClass/edit/<int:pk>', views.ChemClassUpdate.as_view(), name='сhemClass_edit'),
    path('сhemClass/delete/<int:pk>', views.ChemClassDelete.as_view(), name='сhemClass_delete'),

    path('prod/', views.ProdList.as_view(), name='prod_list'),
    path('prod/view/<int:pk>', views.ProdView.as_view(), name='prod_view'),
    path('prod/new', views.ProdCreate.as_view(), name='prod_new'),
    path('prod/view/<int:pk>', views.ProdView.as_view(), name='prod_view'),
    path('prod/edit/<int:pk>', views.ProdUpdate.as_view(), name='prod_edit'),
    path('prod/delete/<int:pk>', views.ProdDelete.as_view(), name='prod_delete'),

    path('ajax/getChildren', views.get_chem_children, name='get_chem_children'),
    path('ajax/getProduction', views.get_chem_products, name='get_chem_products'),
]
