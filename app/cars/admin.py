from django.contrib import admin
from cars.models import *


class ChemClassInline(admin.TabularInline):
    model = ChemClass


class EiInline(admin.StackedInline):
    model = EI


class ProdInline(admin.StackedInline):
    model = Prod


class EIAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_name', 'code']
    list_filter = ['name']
    inlines = [ChemClassInline]


class ChemClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_name', 'main_class', 'base_ei']
    inlines = [ChemClassInline]


class ProdAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_name', 'id_class', 'type_prod', 'conf']
    list_filter = ['name']



class EnumAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_name']
    list_filter = ['name', 'short_name']


class TypeParAdmin(admin.ModelAdmin):
    list_display = ['name_type']
    list_filter = ['name_type']


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['surname', 'name', 'address', 'phone']
    list_filter = ['surname', 'name', 'address']


class ChemClassInline(admin.StackedInline):
    model = ChemClass


class ParameterAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_name', 'ei_par', 'id_enum', 'id_type']
    list_filter = ['name', 'short_name']


# class ParClassAdmin(admin.ModelAdmin):
#     list_display = ['id_par', 'id_class', 'min_val', 'max_val']


class EnumValAdmin(admin.ModelAdmin):
    list_display = ['num', 'name', 'short_name', 'id_enum']
    list_filter = ['name', 'short_name']


class MaterialsAdmin(admin.ModelAdmin):
    list_display = ['id_prod', 'id_material', 'val']


class OrdAdmin(admin.ModelAdmin):
    list_display = ['num', 'date_reg', 'customer']
    list_filter = ['customer']


class ParProdAdmin(admin.ModelAdmin):
    list_display = ['id_par', 'id_prod', 'val', 'note', 'id_val']


class PosOrdAdmin(admin.ModelAdmin):
    list_display = ['num_pos', 'id_order', 'id_prod', 'sums']


admin.site.register(EI, EIAdmin)
admin.site.register(ChemClass, ChemClassAdmin)
admin.site.register(Prod, ProdAdmin)
admin.site.register(Enum, EnumAdmin)
admin.site.register(TypePar, TypeParAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Parameter, ParameterAdmin)
# admin.site.register(ParClass, ParClassAdmin)
admin.site.register(EnumVal, EnumValAdmin)
admin.site.register(Materials, MaterialsAdmin)
admin.site.register(Ord, OrdAdmin)
admin.site.register(ParProd, ParProdAdmin)
admin.site.register(PosOrd, PosOrdAdmin)
