# Generated by Django 3.2.8 on 2021-10-31 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SpamByterApp', '0005_alter_spamusers_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genusers',
            name='PhoneNo',
            field=models.CharField(max_length=13),
        ),
    ]
