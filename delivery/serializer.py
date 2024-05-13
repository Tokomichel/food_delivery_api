from rest_framework import serializers
from .models import *


class Client_serializer(serializers.Serializer):
    # user_id = serializers.IntegerField(source='id')
    # utilisateur = serializers.CharField(max_length = 10)
    # nom = serializers.CharField(max_length = 20)
    # prenom = serializers.CharField(max_length = 20)
    email = serializers.EmailField()
    password = serializers.CharField()

    # sexe = serializers.CharField(max_length = 1)
    # telephone = serializers.CharField(max_length = 9)
    # date_naissance = serializers.DateField(source='birthdate')

    def create(self, validated_data):
        print(validated_data['date_naissance'])

        client = Client()
        client.nom = validated_data["nom"]
        client.prenom = validated_data["prenom"]
        client.email = validated_data["email"]
        client.sexe = validated_data["telephone"]
        client.birthdate = validated_data['date_naissance']
        client.utilisateur = client.nom.lower() + "_" + client.prenom.lower()

        client.save()

        return client

    def update(self, instance: Client, validated_data):
        client = Client.objects.get(utilisateur=instance.utilisateur)
        client.nom = instance.nom
        client.prenom = instance.prenom
        client.email = instance.email
        client.sexe = instance.sexe
        client.password = instance.password
        client.telephone = instance.telephone
        client.birthdate = instance.birthdate
        client.utilisateur = client.nom.lower() + "_" + client.prenom.lower()

        client.save()
        return instance

    class Meta:
        model = Client


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
    plat = Plat_serializer(many=True, read_only=True)

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
            'date_commande',
            'date_debut_cuisson',
            'date_debut_livraison',
            'date_fin_livraison',
            'recu',
            'repas'
        ]
