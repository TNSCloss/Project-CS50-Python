import hashlib
import re
import base64
from cryptography.fernet import Fernet

def main():
    print("=== CyberSecurity ToolKit ===")
    print("1. Verificar força de senha")
    print("2. Gerar hash de arquivo")
    print("3. Checar se senha está comprometida")
    print("4. Criptografar mensagem")
    print("5. Descriptografar mensagem")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        senha = input("Digite a senha: ")
        print(check_password_strength(senha))
    elif escolha == "2":
        caminho = input("Digite o caminho do arquivo: ")
        print(hash_file(caminho))
    elif escolha == "3":
        senha = input("Digite a senha: ")
        print(check_password_compromised(senha))
    elif escolha == "4":
        mensagem = input("Digite a mensagem: ")
        chave = generate_key()
        criptografada = encrypt_message(mensagem, chave)
        print("Mensagem criptografada:", criptografada)
        print("Chave usada:", chave.decode())
    elif escolha == "5":
        chave = input("Digite a chave: ").encode()
        mensagem = input("Digite a mensagem criptografada: ")
        print("Mensagem original:", decrypt_message(mensagem, chave))
    else:
        print("Opção inválida.")


def check_password_strength(password: str) -> str:
    if len(password) < 8:
        return "Senha fraca: menos de 8 caracteres."
    if not re.search(r"[A-Z]", password):
        return "Senha fraca: falta letra maiúscula."
    if not re.search(r"[a-z]", password):
        return "Senha fraca: falta letra minúscula."
    if not re.search(r"[0-9]", password):
        return "Senha fraca: falta número."
    if not re.search(r"[@$!%*?&]", password):
        return "Senha fraca: falta caractere especial."
    return "Senha forte!"


def hash_file(filepath: str) -> str:
    try:
        sha256 = hashlib.sha256()
        with open(filepath, "rb") as f:
            for bloco in iter(lambda: f.read(4096), b""):
                sha256.update(bloco)
        return sha256.hexdigest()
    except FileNotFoundError:
        return "Arquivo não encontrado."


def check_password_compromised(password: str) -> str:
    compromised_list = ["123456", "password", "qwerty", "abc123"]
    if password in compromised_list:
        return "Senha comprometida! Não use."
    return "Senha não encontrada em listas conhecidas."


def generate_key() -> bytes:
    """Gera uma chave secreta para criptografia."""
    return Fernet.generate_key()


def encrypt_message(message: str, key: bytes) -> str:
    """Criptografa uma mensagem usando AES (Fernet)."""
    f = Fernet(key)
    token = f.encrypt(message.encode())
    return base64.urlsafe_b64encode(token).decode()


def decrypt_message(token: str, key: bytes) -> str:
    """Descriptografa uma mensagem usando AES (Fernet)."""
    f = Fernet(key)
    decrypted = f.decrypt(base64.urlsafe_b64decode(token))
    return decrypted.decode()


if __name__ == "__main__":
    main()
