# Generated by Django 4.1.1 on 2022-10-05 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dosen', '0002_alter_dosen_nidn_alter_dosen_nip_alter_dosen_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dosen',
            name='nidn',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='dosen',
            name='nip',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='dosen',
            name='no',
            field=models.IntegerField(),
        ),
    ]
