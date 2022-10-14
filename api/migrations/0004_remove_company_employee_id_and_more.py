# Generated by Django 4.1.2 on 2022-10-14 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_remove_employee_company_name_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="company", name="Employee_id",),
        migrations.RemoveField(model_name="department", name="Employee_id",),
        migrations.AddField(
            model_name="employee",
            name="company",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="api.company",
            ),
        ),
        migrations.AddField(
            model_name="employee",
            name="department",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="api.department",
            ),
        ),
    ]
