# Generated by Django 3.1.1 on 2020-09-24 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customers", "0002_auto_20200923_1952"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="email",
            field=models.EmailField(
                default="acb@app.com", max_length=254, unique=True
            ),  # noqa
            preserve_default=False,
        ),
    ]
