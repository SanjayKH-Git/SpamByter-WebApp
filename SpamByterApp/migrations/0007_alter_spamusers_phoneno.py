# Generated by Django 3.2.8 on 2021-10-31 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SpamByterApp', '0006_alter_genusers_phoneno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spamusers',
            name='PhoneNo',
            field=models.CharField(max_length=13),
        ),
    ]