from django.db import models

# Create your models here.
class Region(models.Model):
    idRegion=models.AutoField(primary_key=True) 
    Nom=models.CharField(max_length=60)
    zoom=models.IntegerField()
    xcoor=models.FloatField()
    ycoor=models.FloatField()

class PointInteret(models.Model):
  idPoint=models.AutoField(primary_key=True)
  Nom=models.CharField(max_length=60)
  longitude=models.FloatField()
  latitude=models.FloatField()
  heureOuverture=models.TimeField()
  heureFermeture=models.TimeField()
  rate=models.IntegerField()
  categorie=models.CharField(max_length=25) 
  theme=models.CharField(max_length=45)
  regionId=models.ForeignKey(Region,on_delete=models.CASCADE,default=None)

class Evenement(models.Model):
    idEvenement=models.AutoField(primary_key=True)
    Nom=models.CharField(max_length=80)
    Description=models.CharField(max_length=400)
    DateDebut=models.DateField()
    DateFin=models.DateField()
    DatePublication=models.DateField(auto_now_add=True)
    PiId=models.ForeignKey(PointInteret,on_delete=models.CASCADE,default=None)
    
class Visiteur(models.Model):
    idVisiteur=models.AutoField(primary_key=True)
    Nom=models.CharField(max_length=60)
    Prenom=models.CharField(max_length=60,null=True)
    Pays=models.CharField(max_length=45)
    NumTel=models.CharField(max_length=10,null=True)
    email=models.EmailField(max_length=254)
    motDePasse=models.CharField(max_length=500)
   

class Commentaire(models.Model):
    idCommentaire=models.AutoField(primary_key=True)
    Contenu=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
    visiteurId=models.ForeignKey(Visiteur,on_delete=models.CASCADE,default=None)
    PiId=models.ForeignKey(PointInteret,on_delete=models.CASCADE,default=None)
    transports=models.ManyToManyField('MoyenTransport')

class MoyenTransport(models.Model):
    idMoyenTransport=models.AutoField(primary_key=True)
    categorie=models.CharField(max_length=50)
    NombrePassagers=models.IntegerField() 



