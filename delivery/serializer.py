from dataclasses import field
from genericpath import exists
from rest_framework import serializers
from .models import *


class My_serializer():

    fields: list
    classe: object
    date_naissance: str = 'birthdate'
    adresse: str = 'email'

    def __init__(self, data: object, fields: list) -> None:
        self.fields = fields
        self.data = data
    
    def get_data(self): 
        many = type(self.data) == list
        final_data: object

        if many:
            final_data = []

            for elt in self.data:
                dic =  {}
                att = elt.__dict__
                for i in self.fields:
                    try:
                        dic[i] = att[i]
                    except Exception:
                        try:
                            serializer = self.__dict__[i]
                        except Exception:
                            raise Exception
                        
                        dic[i] = serializer
                
                final_data.append(dic)
        
        else:
            
            dic =  {}
            att = self.data.__dict__
            for i in self.fields:
                try:
                    dic[i] = att[i]
                except Exception:
                    try:
                        serializer = getattr(self, i, "attribut non trouve")
                    except Exception:
                        print(f" i: {i}  self.dic: {self.__dict__}")
                        ge = getattr(self, i, "attribut non trouve")
                        print(f"{ge}")
                        return {}
                    
                    print("pas d'exception")
                    dic[i] = att[serializer]
            
            final_data = dic
        
        return final_data


class Client_serializer(serializers.Serializer):

    class Meta:
        model = Client
        fields = ['utilisateur', 'nom', 'prenom', 'email', 'sexe', 'telephone', 'date_naissance']


class Plat_serializer(serializers.ModelSerializer):

    class Meta:
        model = Plat
        fields = ['nom', 'image_url', 'temps_cuisson']


class Rest_serializer(serializers.ModelSerializer):
    plats = Plat_serializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = ['nom', 'localisation', 'note', 'plats']


class Repas_serializer(serializers.ModelSerializer):
    plat = Plat_serializer(read_only=True)


    class Meta:
        model = Repas
        fields = ['id', 'plat', 'commande', 'quantite']


class Com_serializer(serializers.ModelSerializer):
    repas = Repas_serializer(many=True, read_only=True)

    class Meta:
        model = Commande
        fields = [
            'id',
            'client',
            'livreur',
            'restaurant',
            'date_commande',
            'date_debut_cuisson',
            'date_debut_livraison',
            'date_fin_livraison',
            'recu',
            'repas'
        ]
