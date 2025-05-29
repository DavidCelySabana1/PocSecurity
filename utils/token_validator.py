from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
from jose import jwk
from jose.utils import base64url_decode
import requests

bearer_scheme = HTTPBearer()
KEYCLOAK_JWKS_URL = "http://keycloak:8080/realms/demo/protocol/openid-connect/certs"

def get_public_key():
    jwks = requests.get(KEYCLOAK_JWKS_URL).json()
    print(f"JWKS: {jwks}", flush=True)  # Debugging line to check the JWKS
    key_data = jwks["keys"][0]
    print(f"Key data: {key_data}", flush=True)  # Debugging line to check the key data
    try:
        key = jwk.construct(key_data)  # puede lanzar una excepción
        print("Clave pública construida:", key, flush=True)
        return key
    except Exception as e:
        print("❌ Error al construir la clave pública:", str(e), flush=True)
        raise
    return key

def validate_token(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    token = credentials.credentials
    #print(f"Validating token: {token}", flush=True)  # Debugging line to check the token
    try:
        public_key = get_public_key()
        print(f"Public key: {public_key}", flush=True)  # Debugging line to check the public key
        payload = jwt.decode(token, public_key, algorithms=["RS256"], audience="account")
        print(f"Decoded payload: {payload}", flush=True)  # Debugging line to check the decoded payload
        return payload
    except Exception:
        raise HTTPException(status_code=401, detail="Token invalido")