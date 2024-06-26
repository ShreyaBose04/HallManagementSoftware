# Generated by Django 5.0.3 on 2024-04-01 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hallmanager',
            options={'permissions': [('is_hall_manager', 'is_hall_manager')]},
        ),
        migrations.AlterModelOptions(
            name='hmc',
            options={'permissions': [('is_HMC', 'is HMC')]},
        ),
        migrations.AlterModelOptions(
            name='messmanager',
            options={'permissions': [('is_mess_manager', 'is_mess_manager')]},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'permissions': [('is_student', 'is_student')]},
        ),
        migrations.AlterModelOptions(
            name='warden',
            options={'permissions': [('is_warden', 'is_warden')]},
        ),
        migrations.AlterField(
            model_name='due',
            name='type',
            field=models.CharField(choices=[('Mess Dues', 'Mess Dues'), ('Hall Dues', 'Hall Dues')], default='mess', max_length=100, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='hallemployee',
            name='paid_monthly_leaves',
            field=models.IntegerField(default=0, verbose_name='Paid leaves'),
        ),
        migrations.AlterField(
            model_name='hallemployee',
            name='unpaid_monthly_leaves',
            field=models.IntegerField(default=0, verbose_name='Unpaid leaves'),
        ),
        migrations.AlterField(
            model_name='halltransaction',
            name='type',
            field=models.CharField(choices=[('Salaries', 'Salaries'), ('Allotment', 'Allotment')], default='salaries', max_length=100, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='month',
            field=models.CharField(choices=[('January', 'January'), ('Febraury', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=20, verbose_name='Month'),
        ),
        migrations.AlterField(
            model_name='messtransaction',
            name='type',
            field=models.CharField(choices=[('Rations', 'Rations'), ('Allotment', 'Allotment')], default='salaries', max_length=100, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='ration',
            name='item2',
            field=models.CharField(blank=True, max_length=20, verbose_name='Item 2'),
        ),
        migrations.AlterField(
            model_name='ration',
            name='qt1',
            field=models.IntegerField(blank=True, verbose_name='Quantity 1'),
        ),
        migrations.AlterField(
            model_name='ration',
            name='qt2',
            field=models.IntegerField(blank=True, verbose_name='Quantity 2'),
        ),
        migrations.AlterField(
            model_name='ration',
            name='qt3',
            field=models.IntegerField(blank=True, verbose_name='Quantity 3'),
        ),
        migrations.AlterField(
            model_name='ration',
            name='qt4',
            field=models.IntegerField(blank=True, verbose_name='Quantity 4'),
        ),
        migrations.AlterField(
            model_name='ration',
            name='qt5',
            field=models.IntegerField(blank=True, verbose_name='Quantity 5'),
        ),
        migrations.AlterField(
            model_name='ration',
            name='rate1',
            field=models.IntegerField(blank=True, verbose_name='Rate 1'),
        ),
        migrations.AlterField(
            model_name='ration',
            name='rate2',
            field=models.IntegerField(blank=True, verbose_name='Rate 2'),
        ),
        migrations.AlterField(
            model_name='ration',
            name='rate3',
            field=models.IntegerField(blank=True, verbose_name='Rate 3'),
        ),
        migrations.AlterField(
            model_name='ration',
            name='rate4',
            field=models.IntegerField(blank=True, verbose_name='Rate 4'),
        ),
        migrations.AlterField(
            model_name='ration',
            name='rate5',
            field=models.IntegerField(blank=True, verbose_name='Rate 5'),
        ),
        migrations.AlterField(
            model_name='wardentransaction',
            name='type',
            field=models.CharField(choices=[('Hall Allotment', 'Hall Allotment'), ('mess Allotment', 'Mess Allotment'), ('Grant', 'Grant')], default='salaries', max_length=100, verbose_name='Type'),
        ),
    ]
