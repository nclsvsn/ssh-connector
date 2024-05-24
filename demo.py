import os
from getpass import getpass

from dotenv import load_dotenv

from sshcon import SshConnector


def _with(sshcon):
    with sshcon as ssh:
        stdin, stdout, stderr = ssh.exec_command("cat /etc/passwd")
        stdin.close()
        output = stdout.read().decode()

    return output


def _call(sshcon):
    return sshcon("ls -lah")


def _main():
    # On charge les variables d'environnement crée dans le fichier ".env"
    load_dotenv()

    # On s'assure d'avoir récupéré le logname et qu'il ne s'agit pas de root
    # Dans le cas contraire, on demande une entrée utilisateur
    if not (username := os.getenv("LOGNAME")) or username == "root":
        username = input(f"Veuillez entrer votre nom d'utilisateur:\n")

    # On s'assure d'avoir récupéré le password
    # Dans le cas contraire, on demande une entrée utilisateur
    if not (password := os.getenv("PASSWORD")):
        password = getpass(f"Veuillez entrer un mot de passe pour l'utilisateur '{username}' :")

    # On crée notre connecteur ssh
    sshcon = SshConnector("localhost", username, password)

    print(_call(sshcon))

    print(_with(sshcon))


if __name__ == "__main__":
    _main()
