from project import check_password_strength, hash_file, check_password_compromised, generate_key, encrypt_message, decrypt_message
import tempfile
import os

def test_check_password_strength():
    assert check_password_strength("abc") == "Senha fraca: menos de 8 caracteres."
    assert check_password_strength("Abcdef12!") == "Senha forte!"

def test_hash_file():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(b"teste")
        tmp_path = tmp.name
    resultado = hash_file(tmp_path)
    os.remove(tmp_path)
    assert isinstance(resultado, str)
    assert len(resultado) == 64

def test_check_password_compromised():
    assert check_password_compromised("123456") == "Senha comprometida! Não use."
    assert check_password_compromised("Segura123!") == "Senha não encontrada em listas conhecidas."

def test_encrypt_decrypt_message():
    key = generate_key()
    mensagem = "Segredo123!"
    criptografada = encrypt_message(mensagem, key)
    descriptografada = decrypt_message(criptografada, key)
    assert descriptografada == mensagem