# EPIC-EVENTS

Développez une architecture (CRM) back-end sécurisée en utilisant ``Python et SQL``.


Ce logiciel CRM permettra de collecter et de traiter les données des clients et de leurs événements, tout en facilitant la communication entre les différents pôles de l'entreprise.

# Fonctionnalités
L'application présente les cas d'utilisations suivantes :

1 - Le département commercial crée et met à jour les profils de leurs clients sur la plateforme. Une fois le contrat signé, le commercial crée l'événement dans la plateforme.  

2 - Lorsqu'un client souhaite organiser une événement, un collaborateur du département gestion crée un contrat et l'associe au client, puis designe un membre su département support qui sera responsable de l'organisation et du déroulé de l'événement

3 - Le département support voit uniquement les événements qui leurs sont attribués et met à jour les événements dont il est responsable.


# Tester le projet

Lancer votre terminal et clonez le projet:

    git clone https://github.com/cedric-joan/Epic-Events


# Installation

Pour faire fonctionner ce site web, suiver les instructions suivantes:
``Python version : 3.9``

Créer un environnement virtuel en utilisant la commande: ``python -m venv env``.

Pour l'activer exécutez la commande: env/bin/activate ou source env/Scripts/activate (sous Windows)

Les dépendances sont listés dans le fichier `requirements.txt`.

Lancer la commande: 
```
pip install -r requirements.txt
```

# Lancer le programme

Allez dans le dossier crm_project/ Lancer la commande:
```
python manage.py runserver
```

Une fois l'API lancée:
```
vous devriez voir dans le terminal Starting development server at http://127.0.0.1:8000/
```
Adresse administrateur:
```
http://127.0.0.1:8000/admin
```
Vous pouvez à présent continuer de suivre les instructions de la documentation sur POSTMAN