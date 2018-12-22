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

]