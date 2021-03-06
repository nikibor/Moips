# Generated by Django 2.1.4 on 2018-12-23 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chemclass',
            name='base_ei',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cars.EI', verbose_name='Базовая ед. измерения'),
        ),
        migrations.AlterField(
            model_name='chemclass',
            name='main_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cars.ChemClass', verbose_name='Родительский класс'),
        ),
        migrations.AlterField(
            model_name='chemclass',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Обозначение класса изделия'),
        ),
        migrations.AlterField(
            model_name='chemclass',
            name='short_name',
            field=models.CharField(max_length=255, verbose_name='Полное имя класса изделия'),
        ),
        migrations.AlterField(
            model_name='ei',
            name='code',
            field=models.IntegerField(verbose_name='Код'),
        ),
        migrations.AlterField(
            model_name='ei',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Полное название'),
        ),
        migrations.AlterField(
            model_name='ei',
            name='short_name',
            field=models.CharField(max_length=40, verbose_name='Единицы измерения'),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='ei_par',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cars.EI'),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='id_enum',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cars.Enum'),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='id_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cars.TypePar'),
        ),
        migrations.AlterField(
            model_name='parclass',
            name='min_val',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='prod',
            name='conf',
            field=models.FloatField(verbose_name='Терминальный класс изделия'),
        ),
        migrations.AlterField(
            model_name='prod',
            name='id_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cars.ChemClass', verbose_name='Класс изделия'),
        ),
        migrations.AlterField(
            model_name='prod',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Полное название изделия'),
        ),
        migrations.AlterField(
            model_name='prod',
            name='short_name',
            field=models.CharField(max_length=40, verbose_name='Обозначение изделия'),
        ),
        migrations.AlterField(
            model_name='prod',
            name='type_prod',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cars.Prod', verbose_name='Родительское изделие'),
        ),
    ]
