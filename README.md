# Onisenpy

Bibliothèque Python servant d'interface Python à l'API de l'ONISEP (http://opendata.onisep.fr/3-api.htm).

Ce script reprend les fonctions mises à dispostion par l'API :

SÉCURITÉ :  
- login : Récupération d'un token valable 24 h pour un développeur enregistré.
  - Méthode : `POST` 

LICENCES :
- licenses : Liste des licences
  - Méthode : `GET`
- licenses_id : Affichage d'une licence liée à un jeu de données désigné par son identifiant.

DONNÉES :
- dataset_code_search : Recherche dans un jeu de données.
  - Méthode : `GET` 

CATALOGUE:
- dataset : Liste des jeux de données.
  - Méthode : `GET`    
- dataset_code : Affichage des métadonnées d'un jeu de données.
    - Méthode : `GET`

APPLICATION:
- application : Liste des applications.
  - Méthode : `GET`
- application_id : Récupération d'une application en spécifiant son identifiant.
  - Méthode : `GET`