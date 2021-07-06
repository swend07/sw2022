# Generated by Django 3.2.4 on 2021-07-01 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("actus", "0011_agendasuivre_heure"),
    ]

    operations = [
        migrations.CreateModel(
            name="Newsletter_model",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.CharField(max_length=150)),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("subscribed", models.BooleanField(default=True)),
            ],
            options={
                "ordering": ["date"],
            },
        ),
    ]
