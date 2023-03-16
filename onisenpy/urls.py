""" Fichier contenant les URL de base pour les requetes sur l'API."""
import os
from enum import StrEnum


BASE_URL = "https://api.opendata.onisep.fr/api/1.0"  # URL utilisée pour les requêtes


# Points d'entrées de l'API
class Url(StrEnum):
    APPLICATION = os.path.join(BASE_URL, "application")
    CATALOGUE = os.path.join(BASE_URL, "dataset")
    LICENCE = os.path.join(BASE_URL, "licenses")
    SECURITE = os.path.join(BASE_URL, "login")
