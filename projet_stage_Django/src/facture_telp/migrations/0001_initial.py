# Generated by Django 4.0.5 on 2022-07-05 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('adresse', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('type', models.CharField(choices=[('b', 'business'), ('s', 'simple')], help_text='simple ou business', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('service_id', models.AutoField(primary_key=True, serialize=False)),
                ('designation', models.CharField(max_length=30)),
                ('prix_unite', models.IntegerField(default=0)),
                ('unite', models.CharField(choices=[('s', 'seconde'), ('o', 'octet'), ('SMS', 'SMS')], help_text='seconde ou octet ou SMS', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='offre',
            fields=[
                ('offre_id', models.AutoField(primary_key=True, serialize=False)),
                ('offre_parent', models.CharField(default='', max_length=30)),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facture_telp.service')),
            ],
        ),
        migrations.CreateModel(
            name='facture',
            fields=[
                ('facture_id', models.AutoField(primary_key=True, serialize=False)),
                ('consom_appel', models.IntegerField(default=0)),
                ('consom_sms', models.IntegerField(default=0)),
                ('consom_internet', models.IntegerField(default=0)),
                ('paid', models.IntegerField(default=0)),
                ('somme_tot', models.IntegerField(default=0)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facture_telp.client')),
            ],
        ),
        migrations.CreateModel(
            name='contrat',
            fields=[
                ('contrat_id', models.AutoField(primary_key=True, serialize=False)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facture_telp.client')),
                ('offre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facture_telp.offre')),
            ],
        ),
    ]
