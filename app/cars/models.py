from django.db import models


class EI(models.Model):
    code = models.IntegerField(
        null=False
    )
    name = models.CharField(
        max_length=255,
        null=False
    )
    short_name = models.CharField(
        max_length=40,
        null=False
    )

    class Meta:
        verbose_name = 'Едиица измерения'
        verbose_name_plural = 'Еденицы измерения'
        db_table = 'ei'

    def __str__(self):
        return self.name


class Enum(models.Model):
    name = models.CharField(
        max_length=255,
        null=False
    )
    short_name = models.CharField(
        max_length=40,
        null=False
    )

    # TODO: verb_name
    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
        db_table = 'enum'

    def __str__(self):
        return self.name


class TypePar(models.Model):
    name_type = models.CharField(
        max_length=255,
        null=False)

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
        db_table = 'type_par'

    def __str__(self):
        return self.name_type


class Customer(models.Model):
    surname = models.CharField(
        max_length=255,
        null=False
    )
    name = models.CharField(
        max_length=255,
        null=False
    )
    address = models.CharField(
        max_length=255,
        null=False
    )
    phone = models.CharField(
        max_length=12,
        null=False
    )

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        db_table = 'customer'

    def __str__(self):
        return self.name + ' ' + self.surname


class ChemClass(models.Model):
    name = models.CharField(
        max_length=255,
        null=False
    )
    short_name = models.CharField(
        max_length=255,
        null=False
    )
    base_ei = models.ForeignKey(
        'EI',
        on_delete=models.CASCADE,
        null=True
    )
    main_class = models.ForeignKey(
        'ChemClass',
        on_delete=models.CASCADE,
        null=True
    )

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
        db_table = 'chem_class'

    def __str__(self):
        return self.name


class Prod(models.Model):
    name = models.CharField(
        max_length=255,
        null=False
    )
    short_name = models.CharField(
        max_length=40,
        null=False
    )
    conf = models.FloatField(
        null=False
    )
    id_class = models.ForeignKey(
        'ChemClass',
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Класс изделия'
    )
    type_prod = models.ForeignKey(
        'Prod',
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Родительское изделие'
    )

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
        db_table = 'prod'

    def __str__(self):
        return self.name


class Parameter(models.Model):
    name = models.CharField(
        max_length=255,
        null=False
    )
    short_name = models.CharField(
        max_length=40,
        null=False
    )
    ei_par = models.ForeignKey(
        'EI',
        on_delete=models.CASCADE,
        null=True
    )
    id_enum = models.ForeignKey(
        'Enum',
        on_delete=models.CASCADE,
        null=True
    )
    id_type = models.ForeignKey(
        'TypePar',
        on_delete=models.CASCADE,
        null=True
    )

    class Meta:
        verbose_name = 'Параметр'
        verbose_name_plural = 'Параметры'
        db_table = 'parametr'

    def __str__(self):
        return self.name


class ParClass(models.Model):
    id_par = models.ForeignKey(
        'Parameter',
        on_delete=models.CASCADE,
        null=False
    )
    id_class = models.ForeignKey(
        'ChemClass',
        on_delete=models.CASCADE,
        null=False
    )
    min_val = models.IntegerField(
        null=True
    )
    max_val = models.IntegerField(
        null=False
    )

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
        db_table = 'par_class'

    def __str__(self):
        return 'ParClass'


class EnumVal(models.Model):
    num = models.FloatField(
        null=False
    )
    name = models.CharField(
        max_length=255,
        null=False
    )
    short_name = models.CharField(
        max_length=40,
        null=False
    )
    id_enum = models.ForeignKey(
        'Enum',
        on_delete=models.CASCADE,
        null=False
    )

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
        db_table = 'enum_val'

    def __str__(self):
        return self.name


# class PosAgr(models.Model):
#     agr_par = models.ForeignKey(
#         'Parameter',
#         on_delete=models.CASCADE,
#         null=False,
#     )
#     id_par = models.ForeignKey(
#         'Parameter',
#         on_delete=models.CASCADE,
#         null=False,
#     )
#     num = models.IntegerField(
#         null=False
#     )
#
#     class Meta:
#         verbose_name = ''
#         verbose_name_plural = ''
#         db_table = 'pos_agr'


class Materials(models.Model):
    id_prod = models.ForeignKey(
        'Prod',
        on_delete=models.CASCADE,
        null=False,
    )
    id_material = models.ForeignKey(
        'Materials',
        on_delete=models.CASCADE,
        null=False,
    )
    val = models.FloatField(
        null=False
    )

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'
        db_table = 'materials'

    def __str__(self):
        return self.val


class Ord(models.Model):
    num = models.IntegerField(
        null=False
    )
    date_reg = models.DateField(
        null=False
    )
    customer = models.ForeignKey(
        'Customer',
        on_delete=models.CASCADE,
        null=False
    )

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
        db_table = 'ord'

    def __str__(self):
        return self.customer.name


class ParProd(models.Model):
    id_par = models.ForeignKey(
        'Parameter',
        on_delete=models.CASCADE,
        null=False,
    )
    id_prod = models.ForeignKey(
        'Prod',
        on_delete=models.CASCADE,
        null=False,
    )
    val = models.FloatField(
        null=False
    )
    note = models.CharField(
        max_length=255,
        null=False
    )
    id_val = models.ForeignKey(
        'EnumVal',
        on_delete=models.CASCADE,
        null=False
    )

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
        db_table = 'par_prod'

    def __str__(self):
        return self.note


class PosOrd(models.Model):
    num_pos = models.IntegerField(
        null=False
    )
    id_order = models.ForeignKey(
        'Ord',
        on_delete=models.CASCADE,
        null=False,
    )
    id_prod = models.ForeignKey(
        'Prod',
        on_delete=models.CASCADE,
        null=False
    )
    sums = models.FloatField(
        null=False
    )

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
        db_table = 'pos_ord'

    def __str__(self):
        return self.sums
