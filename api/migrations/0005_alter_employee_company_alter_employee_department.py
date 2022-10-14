# Generated by Django 4.1.2 on 2022-10-14 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_remove_company_employee_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="company",
            field=models.ForeignKey(
                default=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="api.company",
            ),
        ),
        migrations.AlterField(
            model_name="employee",
            name="department",
            field=models.ForeignKey(
                default=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="api.department",
            ),
        ),
    ]
