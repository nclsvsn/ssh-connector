# Présentation
Connecteur SSH permettant d'exécuter des commandes.

# Récupération du projet

```bash
git clone https://github.com/nclsvsn/ssh-connector.git
```

# Création de l'environnement virtuel
```bash
cd ssh-connector
python3 -m venv .venv
```

# Installation de dépendances
```bash
. .venv/bin/activate
pip install -r requirements.txt
```

# Ajout des credentials 
Modifiez le fichier ".env" pour y renseigner les champs username et password.


# Lancement du script
```bash
python3 sshcon.py
```
