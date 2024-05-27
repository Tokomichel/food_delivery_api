from django.contrib import admin
from .models import *

class ClientAdminView(admin.ModelAdmin):
    list_display = ['id','utilisateur', 'nom', 'prenom', 'password', 'email',  'birthdate', 'sexe']

class LivreurAdminView(admin.ModelAdmin):
    list_display = ['id', 'nom', 'prenom', 'note', 'sexe']

class RestaurantAdminView(admin.ModelAdmin):
    list_display = ['id', 'nom', 'localisation', 'note']

class PlatAdminView(admin.ModelAdmin):
    list_display = ['nom', 'temps_cuisson', 'restaurant']

class RepasAdminView(admin.ModelAdmin):
    list_display = ['plat', 'commande', 'quantite']

class CommandeAdminView(admin.ModelAdmin):
    list_display = ['id', 'client', 'Livreur', 'date_commande', 'recu']
    
    def Livreur(self, obj):
        print(f"objet: {obj}")
        liv = Livreur.objects.get(id=int(obj.livreur))

        return liv

# Register your models here.

admin.site.register(Client, ClientAdminView)
admin.site.register(Livreur, LivreurAdminView)
admin.site.register(Restaurant, RestaurantAdminView)
admin.site.register(Plat, PlatAdminView)
admin.site.register(Repas, RepasAdminView)
admin.site.register(Commande, CommandeAdminView)

admin.site.site_title = "TORUKA SYSTEM"
admin.site.site_header = "TORUKA SYSTEM" 
admin.site.index_title = "TORUKA SYSTEM"



# {
#     "nom": "Boundeu",
#     "prenom": "Ange",
#     "email": "angeto@gmail.com",
#     "sexe": "H",
#     "telephone": "671719255",
#     "password": "toko26",
#     "date_naissance": "2002-01-26"
# }