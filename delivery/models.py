from django.db import models
from django.db.models import CharField

# Create your models here.
GENRE = [("H", "Homme"), ("F", "Femme")]


class Client(models.Model):
    utilisateur = models.CharField(max_length=100, unique=True, verbose_name="Nom utilisateur")
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    email = models.EmailField(verbose_name="E-mail", unique=True)
    password = models.CharField(max_length=40)
    sexe = models.CharField(max_length=1, choices=GENRE)
    telephone = models.CharField(max_length=9)
    birthdate = models.DateField(verbose_name="Date de naissance")

    def __str__(self) -> str:
        return self.nom + " " + self.prenom


class Location(models.Model):
    nom_lieu = models.CharField(max_length=10)
    location_gm = models.CharField(max_length=200)
    client = models.ForeignKey(to='Client', on_delete=models.PROTECT)


class Livreur(models.Model):
    ETAT = [('L', 'Livraison'), ('A', 'Attente'), ('O', 'Off')]

    utilisateur = models.CharField(max_length=10, unique=True, verbose_name="nom utilisateur")
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    email = models.EmailField(verbose_name="E-mail")
    password = models.CharField(max_length=40)
    sexe = models.CharField(max_length=1, choices=GENRE)
    telephone = models.CharField(max_length=9)
    note = models.FloatField(verbose_name="Moyenne des notes", default=0)
    etat = models.CharField(max_length=1, choices=ETAT, default='O')

    def __str__(self) -> str:
        return self.nom


class Restaurant(models.Model):
    nom = models.CharField(max_length=20)
    localisation = models.TextField()
    note = models.FloatField(default=0)

    def __str__(self) -> CharField:
        return self.nom


class Plat(models.Model):
    nom = models.CharField(max_length=20)
    image_url = models.CharField(max_length=200)
    temps_cuisson = models.IntegerField()
    restaurant = models.ForeignKey(to="Restaurant", on_delete=models.PROTECT, related_name='plats') 

    def __str__(self) -> str:
        return self.nom


class Commande(models.Model):
    client = models.ForeignKey(to="Client", on_delete=models.PROTECT, related_name='commandes')
    restaurant = models.ForeignKey(to='Restaurant', on_delete=models.PROTECT, related_name='commandes')
    livreur = models.CharField(max_length=10, null=True)  # ce champs sera rempli par l'id du livreur des qu'il aura accepte la commande
    date_commande = models.DateField()
    date_debut_cuisson = models.DateField(null=True)
    date_fin_cuisson = models.DateField(null=True)
    date_debut_livraison = models.DateField(null=True)
    date_fin_livraison = models.DateField(null=True)
    recu = models.BooleanField()

    # def __str__(self) -> str:
    #     return str(self.date_commande)


class Repas(models.Model):
    plat = models.ForeignKey(to="Plat", on_delete=models.PROTECT, related_name='plat')
    commande = models.ForeignKey(to="Commande", on_delete=models.PROTECT, related_name='repas')
    quantite = models.IntegerField()

    def __str__(self) -> str:
      return self.nom
