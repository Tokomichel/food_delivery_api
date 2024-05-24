from django.shortcuts import HttpResponse
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .serializer import Client_serializer, Rest_serializer, Com_serializer
from .models import *
from rest_framework.views import APIView


def rand_number(model: models.Model):
    clients = len(model.objects.all())
    return str(clients + 1)

# Create your views here.

def test(req):
    return HttpResponse("<h3 align= 'center'> Hello </h3>")


class Api_client(APIView):

    def get(self, request: Request):
        request
        try:
             client = Client.objects.get(password=request.data['password'], email=request.data['email'])
        except Client.DoesNotExist or KeyError:
            return Response(data={"infos":"mot de passe ou email errone"}, status=status.HTTP_400_BAD_REQUEST)

        data = {
            "utilisateur": f"{client.utilisateur}",
            "nom": f"{client.nom}",
            "prenom": f"{client.prenom}",
            "email": f"{client.email}",
            "sexe": f"{client.sexe}",
            "telephone": f"{client.telephone}",
            "date_naissance": f"{client.birthdate}"
        }

        return  Response(data=data, status=status.HTTP_200_OK)
    
    def post(self, request: Request):
        print(request.data)

        try:
            pw = request.data['nom']
            
            client = Client()

            client.nom = request.data["nom"]
            client.prenom = request.data['prenom']
            client.email = request.data['email']
            client.sexe = request.data['sexe']
            client.password = request.data['password']
            client.telephone = request.data['telephone']
            client.birthdate = request.data['date_naissance']

            client.utilisateur = client.nom + client.prenom + "_" + client.sexe + "_" + rand_number(Client)

            try:
                client.save()
            except Exception:
                client.utilisateur = client.nom + client.prenom + "_" + client.sexe + rand_number()
            
            return Response(data={"infos": f"{client.nom} enregistre avec succes"}, status=status.HTTP_201_CREATED )

            
            
        except Exception:   
            try:
                client = Client.objects.get(password=request.data['password'], email=request.data['email'])
            except Client.DoesNotExist or KeyError:
                return Response(data={"infos":"mot de passe ou email errone"}, status=status.HTTP_400_BAD_REQUEST)

            data = {
                "utilisateur": f"{client.utilisateur}",
                "nom": f"{client.nom}",
                "prenom": f"{client.prenom}",
                "email": f"{client.email}",
                "sexe": f"{client.sexe}",
                "telephone": f"{client.telephone}",
                "date_naissance": f"{client.birthdate}"
            }

            return  Response(data=data, status=status.HTTP_200_OK)


    
    def put(self, req: Request):
        try:
            client = Client.objects.get(utilisateur=req.data['user_name'])
        except Client.DoesNotExist:
            return Response(data={"infos": "erreur"}, status=status.HTTP_400_BAD_REQUEST)
        
        data = req.data
        client.nom = data['nom']
        client.prenom = data["prenom"]
        client.sexe = data['sexe']
        client.password = data['password']
        client.email = data['email']
        client.telephone = data['telephone']
        client.birthdate = data['date_naissance']


        client.save()
        return Response({"infos": "changements sauvegarder avec succes"}, status=status.HTTP_202_ACCEPTED)


class Api_restaurant(APIView):

    def get(self, request: Request):
        restaurants = Restaurant.objects.all()

        seri = Rest_serializer(data=restaurants, many=True)
        valid = seri.is_valid() is not True

        if valid:
            print("bonne requete vers restaurant")
            return Response(seri.data, status=status.HTTP_200_OK)
        
        else:
            return Response(data={"infos": "non valide"}, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, req: Request):

        restaurant = Restaurant()
        restaurant.nom = req.data['nom']
        restaurant.localisation = req.data['localisation']
        
        if restaurant.note == 0:
            restaurant.note = req.data['note']
        else:
            note = (float(req.data['note']) + restaurant.note) / 2
            restaurant.note = note

        try:
            restaurant.save()
        except Exception:
            return Response({"infos": "an error occured"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"infos": f"{restaurant.nom} ajouter avec succes"}, status.HTTP_200_OK)


class Api_livreur(APIView):

    def get(self, req: Request):
        try:
            liv = Livreur.objects.get(email=req.data['email'], password=req.data['password'])
        except Exception:
            return Response({"infos":"Erreur"}, status.HTTP_400_BAD_REQUEST)
        
        data = {
            "utilisateur": liv.utilisateur,
            "nom": liv.nom,
            "prenom": liv.prenom,
            "email": liv.email,
            "sexe": liv.sexe,
            "telephone": liv.telephone,
            "note": liv.note,
            "etat": liv.etat
        }

        return Response(data, status.HTTP_200_OK)
    
    def post(self, req: Request):
        print(req.data)
        try:
            print("insertion")
            liv = Livreur()
            data = req.data

            liv.nom = data["nom"]
            liv.prenom = data["prenom"]
            liv.email = data["email"]
            liv.password = data['password']
            liv.sexe = data['sexe']
            liv.telephone = data['telephone']
            liv.etat = data['etat']

            liv.utilisateur = liv.nom + liv.prenom + "_" + liv.sexe + "_" + rand_number(Livreur)

            if liv.note == 0:
                liv.note = data['note']
            else:
                note = (float(data['note']) + liv.note) / 2
                liv.note = note

            try:
                liv.save()

            except Exception:
                return Response({"infos": "erreur"}, status.HTTP_400_BAD_REQUEST)

            return Response({"infos": f"{liv.nom} ajouter avec succes"})
        
        except Exception:
            print(f"authentification \t {Exception.args}")
            try:
                    liv = Livreur.objects.get(email=req.data['email'], password=req.data['password'])
            except Exception:
                    return Response({"infos":"Erreur"}, status.HTTP_400_BAD_REQUEST)

            data = {
                "utilisateur": liv.utilisateur,
                "nom": liv.nom,
                "prenom": liv.prenom,
                "email": liv.email,
                "sexe": liv.sexe,
                "telephone": liv.telephone,
                "note": liv.note,
                "etat": liv.etat
            }
            return Response(data, status.HTTP_200_OK)
    

class One_livreur(APIView):
    def get(self, req: Request, id):
        pass


class Api_commande(APIView):

    def get(self, req: Request):
        objs = Commande.objects.all()

        ser = Com_serializer(data=objs, many=True)
        val = ser.is_valid()
        print(val)
        return Response(data=ser.data, status=status.HTTP_200_OK)
    
    def post(self, req: Request):
        com = Commande()

        com.client = Client.objects.get(id=req.data["client"])
        com.livreur = req.data['livreur']
        com.date_commande = req.data['date_commande']
        com.date_debut_cuisson = req.data['date_debut_cuisson']
        com.date_fin_cuisson = req.data['date_fin_cuisson']
        com.date_debut_livraison = req.data['date_debu_livraison']
        com.date_fin_livraison = req.data['date_fin_livraison']
        com.recu = req.data['recu']
         
        return
