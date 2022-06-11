EPIC EVENT  : Développement d'un architecture back-end sécurisée en utilisant Django ORM

Utilisation :

- Django
- Django Rest
- Postman
- PostgreSQL
- pgAdmin 4


l'API a deux application : 
- account
- crm

Installation : 

- Installer Python 3.9.1
- Téléchargez le package d'application depuis github, décompressez-le et stockez-le dans un nouveau répertoire.
- Dans le fichier settings.py, dans la partie DATABASES, modifiez le USER et le PASSWORD en fonction de vos paramètres postgreSQL.
- Créer un environnement virtuel <code>python -m venv env</code>
- Activer l'environnement virtuel <code>venv\Scripts\activate.bat</code>
- Installez la dernière version de <code>pip python -m pip install --upgrade pip </code>
- Installez les packages Python externes avec <code>pip install -r requirements.txt </code>
- Dans pgAdmin 4, créez une base de données my_db
- <code>python manage.py makemigrations</code>
- <code>python manage.py migrate</code>

Utilisation : 

- Exécutez l'API server <code>python manage.py runserver</code>
- Accès à l'interface d'administration django de l'application à l'URL http://127.0.0.1:8000/admin
- créer un compte super-utilisateur  <code>python manage.py createsuperuser</code>
