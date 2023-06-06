from asyncio.windows_events import NULL
from msilib.schema import Class
from django.db import models
from django.forms import PasswordInput

# Create your models here.
"""
client :
id,nom, prénom, adresse, email, type (simple, business)
"""

class client (models.Model):
    client_id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    adresse = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    type_choices =(("b", "business"),("s","simple"))
    type = models.CharField(help_text="simple ou business", max_length=10 , choices= type_choices  )




"""
Service  :
Service ID, Désignation, prix par unité, unité (Seconde, Octet, SMS)
"""
class service (models.Model):
    service_id = models.AutoField(primary_key=True)
    designation = models.CharField(max_length=30)
    prix_unite = models.IntegerField(default=0)
    unite_choices =(("s","seconde"), ("o","octet") ,("SMS","SMS"))
    unite = models.CharField(help_text="seconde ou octet ou SMS", max_length=10 , choices= unite_choices  )
"""
offre  :
offre ID, Désignation, service ID
"""
class offre (models.Model):
    offre_id = models.AutoField(primary_key=True)
    offre_parent  = models.CharField(default='',max_length=30)
    service_id = models.ForeignKey(service, on_delete=models.CASCADE)

"""
contrat  :
contrat ID, client ID, offre ID, service ID. 
"""

class contrat (models.Model):
    contrat_id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(client, on_delete=models.CASCADE)
    offre_id = models.ForeignKey(offre, on_delete=models.CASCADE)

"""
facture   :
facture ID, client ID, quant de consom pour appel , quant de consom pour sms ,quant de consom pour internet """

class facture (models.Model):
    facture_id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(client, on_delete=models.CASCADE)
    consom_appel = models.IntegerField(default=0)
    consom_sms = models.IntegerField(default=0)
    consom_internet = models.IntegerField(default=0)
    paid = models.IntegerField(default=0)
    somme_tot = models.IntegerField(default=0)

"""
User  : username , password
"""
class User(models.Model):
    userName = models.CharField(primary_key=True , max_length=10)
    password = models.IntegerField()

