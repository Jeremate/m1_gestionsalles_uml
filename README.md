# m1_gestionsalles_uml
Projet de gestion de salles développé en Python

## Developer
Section à destination des développeurs

Utilisation de :
- Python 3.4
- git-flow pour la gestion du workflow;
- pyvenv pour les environnements virtuels.

### Environnement virtuel
- créer l'environnement virtuel : pyvenv _nomVenv_
- l'activer : source _nomVenv_/bin/activate
- travailler sur le projet
- enregistrer les dépendances : pip freeze > requirements.txt
- quitter : deactivate

--> ajouter l'environnement virtuel au fichier .gitignore

### Git et Gitflow
- récupérer le travail des autres : git pull
- partager son travail de la branche develop : git push origin develop
- sinon utiliser les commandes git flow

### Utilisation de py.test
- Dans un Terminal, à la racine du projet, exécuter : python3 setup.py test