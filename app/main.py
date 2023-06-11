from fastapi import FastAPI, Depends

from app.vigenaire_сipher import VigenaireСipher

app = FastAPI(docs_url='/', redoc_url='/redoc', title='Vigenare Cipher API')

def get_cipher():
    return VigenaireСipher()

@app.get('/api/v1/encrypt/{text}/{key}/{iterations}')
def encrypt(text: str, key: str, iterations: int = 1, *, cipher: VigenaireСipher = Depends(get_cipher)):
    return cipher.encrypting(text, key, iterations)

@app.get('/api/v1/decrypt/{text}/{key}/{iterations}')
def decrypt(text: str, key: str, iterations: int = 1, *, cipher: VigenaireСipher = Depends(get_cipher)):
    return cipher.decrypting(text, key, iterations)


