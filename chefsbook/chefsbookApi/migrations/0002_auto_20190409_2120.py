# Generated by Django 2.2 on 2019-04-09 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chefsbookApi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='table',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='chefsbookApi.Table'),
        ),
    ]
