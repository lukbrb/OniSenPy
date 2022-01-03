""" Fichier contenant les URL de base pour les requetes sur l'API."""
import os

ACCUEIL = "http://opendata.onisep.fr/3-api.htm"   # URL dd'accueil de l'API
BASE = "https://api.opendata.onisep.fr/api/1.0"  # URL utilisée pour les requêtes

LICENCE = os.path.join(BASE, "licenses")
DATASET = os.path.join(BASE, "dataset")
APPLICATION = os.path.join(BASE, "application")
LOGIN = os.path.join(BASE, "login")

