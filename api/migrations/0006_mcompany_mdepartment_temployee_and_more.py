# Generated by Django 4.1.1 on 2022-10-14 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_employee_company_alter_employee_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='MCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('delete_status', models.BooleanField(blank=True, null=True)),
                ('created_user_id', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_user_id', models.CharField(max_length=100)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('delete_status', models.BooleanField(blank=True, null=True)),
                ('created_user_id', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_user_id', models.CharField(max_length=100)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('delete_status', models.BooleanField(blank=True, null=True)),
                ('created_user_id', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_user_id', models.CharField(max_length=100)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.mcompany')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.mdepartment')),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='company',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='department',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
