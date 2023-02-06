# Guibert Marie 

import requests

contenu = requests.get("http://api.open-notify.org/astros.json")
for personne in contenu.json()["people"]:
    if personne["craft"]=='ISS':
          print(personne)

# git init : initialisation d'un nouveau dépôt
# git status : fichier non suivi
# après git add astronautes.py --> git status : fichier suivi mais pas de commit encore
# git commit -m"Liste des astronautes dans l'espace"
# après le commit : git status --> astronautes.py n'apparaît plus

# git log : présente les différents commits
# informations stockées : 
# author / date / titre du commit