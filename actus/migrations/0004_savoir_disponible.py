# Generated by Django 3.2.4 on 2021-06-29 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("actus", "0003_alter_savoir_numero"),
    ]

    operations = [
        migrations.AddField(
            model_name="savoir",
            name="disponible",
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
