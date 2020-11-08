# Generated by Django 3.1.2 on 2020-11-08 20:05

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [("invoice", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="TaxSetUp",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("country", django_countries.fields.CountryField(max_length=2)),
                ("tax", models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name="invoice",
            name="tax",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="invoice.taxsetup"
            ),
        ),
    ]
