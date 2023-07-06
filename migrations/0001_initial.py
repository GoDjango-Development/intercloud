# Generated by Django 4.1 on 2022-09-19 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ICFExampleProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Recommended resolution 400x300', upload_to='productos/', verbose_name='Image')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('price', models.FloatField(default=0, help_text='Opcional', verbose_name='Price')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Product description')),
                ('is_featured', models.BooleanField(default=False, verbose_name='Es especial?')),
                ('in_stock', models.BooleanField(default=True, verbose_name='Quedan existencias en la tienda?')),
                ('amount', models.FloatField(default=0, verbose_name='Cantidad en el almacen')),
                ('unit', models.CharField(default='', help_text='Por ejemplo: Unidades, Kilogramos, Libras, Litros etc...', max_length=40, verbose_name='Unidad de medida')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='Cantidad de veces que este producto fue visto')),
                ('buys', models.PositiveIntegerField(default=0, verbose_name='Cantidad de veces que este producto fue comprado')),
                ('category', models.CharField(default='', max_length=50, verbose_name='Categoria del producto')),
            ],
        ),
    ]
