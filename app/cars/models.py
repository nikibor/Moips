from django.db import models


class EI(models.Model):
    code = models.IntegerField(
        null=False,
        verbose_name='Код'
    )
    name = models.CharField(
        max_length=255,
        null=False,
        verbose_name='Полное название'
    )
    short_name = models.CharField(
        max_length=40,
        null=False,
        verbose_name='Единицы измерения'
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
        verbose_name = 'Перечисление параметров обвесов'
        verbose_name_plural = 'Перечисления параметров обвесов'
        db_table = 'enum'

    def __str__(self):
        return self.name


class TypePar(models.Model):
    name_type = models.CharField(
        max_length=255,
        null=False)

    class Meta:
        verbose_name = 'Тип параметров обвесов'
        verbose_name_plural = 'Типы параметров обвесов'
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
        null=False,
        verbose_name='Обозначение класса изделия'
    )
    short_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Полное имя класса изделия'
    )
    base_ei = models.ForeignKey(
        'EI',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Базовая ед. измерения'
    )
    main_class = models.ForeignKey(
        'ChemClass',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Родительский класс'
    )

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'
        db_table = 'chem_class'

    def __str__(self):
        return self.name


class Prod(models.Model):
    name = models.CharField(
        max_length=255,
        null=False,
        verbose_name='Полное название изделия'
    )
    short_name = models.CharField(
        max_length=40,
        null=False,
        verbose_name='Обозначение изделия'
    )
    conf = models.FloatField(
        null=False,
        verbose_name='Терминальный класс изделия'
    )
    id_class = models.ForeignKey(
        'ChemClass',
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Класс изделия',
        blank=True
    )
    type_prod = models.ForeignKey(
        'Prod',
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Родительское изделие',
        blank=True
    )

    class Meta:
        verbose_name = 'Изделие'
        verbose_name_plural = 'Изделия'
        db_table = 'prod'

    def __str__(self):
        return self.name

    # def chem_classes(self):
    #     return ChemClass.objects.filter(id=self.id_class.name)


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
        null=True,
        blank=True
    )
    id_enum = models.ForeignKey(
        'Enum',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    id_type = models.ForeignKey(
        'TypePar',
        on_delete=models.CASCADE,
        null=True,
        blank=True
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
        null=True,
        blank=True
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
        verbose_name = 'Вариан параметров'
        verbose_name_plural = 'Варианты параметров'
        db_table = 'enum_val'

    def __str__(self):
        return self.name


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
        return self.id_prod.name


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
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
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
        verbose_name = 'Параметр изделия'
        verbose_name_plural = 'Параметры изделия'
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
        verbose_name = 'Состав заказа'
        verbose_name_plural = 'Состав заказов'
        db_table = 'pos_ord'

    def __str__(self):
        return self.id_prod.name
