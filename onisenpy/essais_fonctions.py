import os
from pprint import pprint
from .func_API import *
from .connexion import Connexion
from .connexion_data import token
USER = os.environ.get("ONISEP_USER")
PASS = os.environ.get("ONISEP_PASS")
dataset_id = "5fa5816ac6a6e"
element_a_chercher = '0195066D'  # code UAI d'une école


def main():
    # conn = Connexion(USER, PASS)
    # conn.save_infos()
    # token = conn.token
    # print("Création :", conn.created_on)
    # print("Expiration :", conn.expire_on)
    # print("Heures restantes :", conn.remaining_time)
    # reponse = dataset_code(dataset_id)

    reponse = data_search(dataset_id, 48.4450915)
    print(reponse.status_code)
    pprint(reponse.headers)
    pprint(reponse.json()["results"])  # créer une méthode pour extraire les liens de téléchargement du jeu de données


if __name__ == "__main__":
    main()
