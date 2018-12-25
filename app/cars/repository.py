from typing import List

from cars.models import ChemClass, Prod


class ChemClassRepository:
    @staticmethod
    def get_child(chem_class_parent_id: int) -> List[ChemClass]:
        return ChemClass.objects.filter(main_class_id=chem_class_parent_id)


class ProdRepository:
    @staticmethod
    def get_class_production(chem_class_id: int) -> List[Prod]:
        return Prod.objects.filter(id_class_id=chem_class_id)
