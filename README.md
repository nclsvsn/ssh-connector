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


# Lancement du script de démo
```bash
python3 demo.py
```

# Import dans un script python
```python
from sshcon import SshConnector

with SshConnector(*credentials) as ssh:
    pass
```
