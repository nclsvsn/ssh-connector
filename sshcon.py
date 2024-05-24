from dataclasses import dataclass
from paramiko import SSHClient, AutoAddPolicy


@dataclass
class SshConnector:
    hostname: str
    username: str
    password: str
    port: int = 22
    _client: SSHClient = None

    def __enter__(self) -> SSHClient:
        self._client = SSHClient()
        self._client.set_missing_host_key_policy(AutoAddPolicy())
        self._client.connect(
            self.hostname,
            self.port,
            self.username,
            self.password
        )
        return self._client

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._client:
            try:
                self._client.close()
            except Exception as e:
                print(f"Erreur lors de la fermeture de la connexion SSH : {e}")

    def __call__(self, command: str) -> tuple[str, str]:
        with self:
            stdin, stdout, stderr = self._client.exec_command(command)
            stdin.close()
            output = stdout.read().decode()
            errors = stderr.read().decode()
        return output, errors
