from fastapi import FastAPI, Depends

from app.vigenaire_сipher import VigenaireСipher

app = FastAPI(docs_url='/', redoc_url='/redoc', title='Vigenare Cipher API')

def get_cipher():
    return VigenaireСipher()

@app.get('/api/v1/encrypt/{text}/{key}/{iterations}')
def encrypt(text: str, key: str, iterations: int = 1, *, cipher: VigenaireСipher = Depends(get_cipher)):
    """
    Метод для шифрония текста при помощи шифра Виженера

    Параметры:
    - text: текст для шифрования
    - key: ключ шифрования
    - iterations: количество итераций шифрования
    """
    return cipher.encrypting(text, key, iterations)

@app.get('/api/v1/decrypt/{text}/{key}/{iterations}')
def decrypt(text: str, key: str, iterations: int = 1, *, cipher: VigenaireСipher = Depends(get_cipher)):
    """
    Метод для дешифрония текста при помощи шифра Виженера

    Параметры:
    - text: текст для дешифрования
    - key: ключ дешифрования
    - iterations: количество итераций дешифрования
    """
    return cipher.decrypting(text, key, iterations)

@app.get('/api/v1/encrypt_decrypt/{text}/{key}/{iterations}')
def encrypt_and_decrypt(text: str, key: str, iterations: int = 1, *, cipher: VigenaireСipher = Depends(get_cipher)):
    """
    Метод для шифрония и дешифрония текста при помощи шифра Виженера

    Параметры:
    - text: текст для шифрования и дешифрования
    - key: ключ шифрования и дешифрования
    - iterations: количество итераций шифрования и дешифрования
    """
    encrypted_text = cipher.encrypting(text, key, iterations)
    decrypted_text = cipher.decrypting(encrypted_text, key, iterations)
    return encrypted_text, decrypted_text