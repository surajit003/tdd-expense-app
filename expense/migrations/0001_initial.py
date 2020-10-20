# Generated by Django 3.1.2 on 2020-10-20 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Expense",
            fields=[
                (
                    "expense_id",
                    models.CharField(
                        default="917c18f4-c5b8-4c3e-bafd-45348b2a3283",
                        max_length=120,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("rent", models.FloatField()),
                ("physio", models.FloatField()),
                ("family", models.FloatField()),
                ("personal", models.FloatField()),
                ("dependent", models.FloatField()),
                ("misc", models.FloatField()),
                ("doctor", models.FloatField()),
                ("gym", models.FloatField()),
                ("saving", models.FloatField()),
                ("extra", models.TextField(blank=True, null=True)),
                ("total", models.FloatField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Expense Detail",
                "verbose_name_plural": "Expense Details",
            },
        )
    ]