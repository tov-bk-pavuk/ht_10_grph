# Generated by Django 3.2.7 on 2021-09-02 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=20, verbose_name='Город')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('availability', models.PositiveIntegerField(verbose_name='Наличие')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Поставщик')),
                ('legal_form', models.CharField(choices=[('TOV', 'TOV'), ('FOP', 'FOP'), ('PAT', 'PAT')], max_length=20, verbose_name='Орг.форма')),
                ('city', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='logistics.city')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='Client', max_length=20, verbose_name='Имя Клиента')),
                ('last_name', models.CharField(max_length=20, verbose_name='Фамилия Клиента')),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logistics.city')),
                ('product', models.ManyToManyField(to='logistics.Product')),
            ],
        ),
    ]