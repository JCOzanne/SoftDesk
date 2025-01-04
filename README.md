# Softdesk

Softdesk support est une API RESTful permettant à ses utilisateurs de créer des projets,  
des tâches et des problèmes pour chaque projet et des commentaires pour faciliter la communication.

## Fonctionnalités

- **Gestion des utilisateurs**  
Les utilisateurs s'identifient avec un username et un password.  
Ils peuvent exprimer explicitement leur consentement sur le fait de pouvoir être contacté  
et de voir leur données partagées.
L'authentification se fait avec un Json Web Token.
-  **Gestion des projets**  
Un utilisateur qui crée un projet en devient également un contributeur.  
Il peut lui attribuer une description et un type (back-end, front-end, iOS ou Android).
- **Créations des tâches et des problèmes**  
Le contributeur d'un projet peut créer une Issue (problème/tâche), la nommer et en donner une description.  
Il peut lui attribuer une priorité (LOW, MEDIUM ou HIGH), sa nature (BUG, FEATURE ou TASK)  
et un statut de progression  (To Do, In Progress ou Finished).
- **Créations des commentaires pour faciliter la communication**  
Les contributeurs d'un projet peuvent créer des Comment (commmentaires) comportant une description  
un lien vers une Issue et un identifiant de type uuid
- **Informations complémentaires**  
Chaque resource comporte un horodatage.  
L’auteur d’une ressource peut modifier ou supprimer cette ressource.  
Les autres utilisateurs ne peuvent que lire la ressource.  
Le contributeur d'une Issue doit pouvoir assigner l’issue à un autre contributeur s’il
le souhaite.  
Seuls les contributeurs peuvent accéder aux ressources qui référencent un projet (l’issue
et le comment).  

## Structure du projet
```
Softdesk/
├── config/               # configuration du projet et urls
├── user/                 # Gestion des utilisateurs
├     ├── models.py/      
├     ├── serializers.py 
├     ├── views.py 
├── project/               # Gestion des projets, issues et comments
├     ├── models.py     
├     ├── serializers.py 
├     ├── views.py 
├     ├── permissions.py 
├── requirements.txt      # Dépendances
└── manage.py             # Commandes Django
└── db.sqlite3            # Base de données
```
# Installation

## Prérequis
- python 3.12
- django 5.1.4
- djangorestframework 5.3.1

## Etapes d'installation
Naviguer dans le dossier souhaité puis :
1. Cloner le dépôt
```
git clone https://github.com/JCOzanne/SoftDesk.git
```
2. Créer et activer l'environnement virtuel  
```
python -m venv .venv
source .venv/bin/activate   # Sur Windows : .venv\Scripts\activate
```
3. Installer les dépendances
```
pip install -r requirements.txt
```
4. Appliquer les migrations  
```
python manage.py migrate
```
5. Lancer le serveur de développement
```
python manage.py runserver
```

# Informations

l'API Softdesk support peut être interrogée à partir des points d'entrée  
commençant par l'url de base http://localhost:8000/api/  

**Liste des utilisateurs existants**

|   Id    |    username    | password    |
|---------|----------------|-------------|
|    1    |     admin      |    admin    |
|    8    |     user_1     |  password_1 |
|    9    |     user_2     |  password_2 |
|   10    |     user_3     |  password_3 |

**Liste des points de terminaison**

| endpoint       | Utilisation                       | Méthode     | Champs                                                                 | Prérequis                      |
|----------------|-----------------------------------|-------------|------------------------------------------------------------------------|--------------------------------|
| token/         | Obtenir un Token                  | POST        | username, password                                                     | Etre identifié                 |
| token/refresh/ | Rafraîchir un token               | POST        | refresh_token                                                          | Etre identifié                 |
| user/          | Créer un utilisateur              | POST        | username, password,<br/>age, consentements                             | -                              |
| user/id/       | Modifier un utilisateur           | PATCH       | <modifier le(s) champ(s)>                                              | Etre l'utilisateur             |
| user/id/       | Supprimer un utilisateur          | DELETE      | -                                                                      | Etre l'utilisateur             |
| user/          | Obtenir la liste des utilisateurs | GET         | -                                                                      | Etre authentifié               |
| project/       | Créer un projet                   | POST        | name, description, type                                                | Etre authentifié               |
| project/id/    | Modifier un projet                | PATCH       | <modifier le(s) champ(s)>                                              | Etre l'auteur, le contributeur |
| project/id/    | Supprimer un projet               | DELETE      | -                                                                      | Etre l'auteur, le contributeur |
| project/       | Obtenir la liste des projets      | GET         | -                                                                      | Etre authentifié               |
| issue/         | Créer une tâche                   | POST        | name, description, priority,<br/>tag, status, project_id<br/>in_charge | Etre l'auteur du projet        |
| issue/id/      | Modifier une tâche                | PATCH       | <modifier le(s) champ(s)>                                              | Etre l'auteur, le contributeur |
| issue/id/      | Supprimer une tâche               | DELETE      | -                                                                      | Etre l'auteur, le contributeur |
| issue/         | Obtenir la liste des tâches       | GET         | -                                                                      | Etre authentifié               |
| comment/       | Créer un commentaire              | POST        | description, issue/id                                                  | Etre l'auteur de l'issue       |
| comment/id/    | Modifier un commentaire           | PATCH       | <modifier le(s) champ(s)>                                              | Etre l'auteur du commentaire   |
| comment/id/    | Supprimer un commentaire          | DELETE      | -                                                                      | Etre l'auteur du commentaire   |
| comment/       | Obtenir la liste des commentaires | GET         | -                                                                      | Etre l'auteur de l'issue       |


En tant qu'auteur d'un projet, je peux attribuer une tâche à un autre utilisateur :  
**Etape 1** : Je déclare cet autre utilisateur en tant que contributeur du projet  
POST http://127.0.0.1:8000/api/contributor/  
champs {"user":user_id, "project":project_id}  
**Etape 2**: Je lui assigne la tâche  
POST http://127.0.0.1:8000/issue/id/  
champ {"in_charge" : user_id }

# Conformité PEP8
Rapport obtenu avec la commande :
flake8 authentication blog webapp --format=html --htmldir=flake8-report 
Conformément au fichier de configuration .flake8
![Rapport Flake8](https://github.com/JCOzanne/SoftDesk/blob/main/rapport_flake8.PNG?raw=true)

