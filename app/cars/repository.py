from typing import List

from cars.models import ChemClass


class ChemClassRepository:
    @staticmethod
    def get_child(chem_class_parent_id: int) -> List[ChemClass]:
        return ChemClass.objects.filter(main_class_id=chem_class_parent_id)
