from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
import requests

bearer_scheme = HTTPBearer()
KEYCLOAK_JWKS_URL = "http://keycloak:8080/realms/demo-realm/protocol/openid-connect/certs"

def get_public_key():
    jwks = requests.get(KEYCLOAK_JWKS_URL).json()
    key = jwks["keys"][0]
    return jwt.construct_rsa_public_key(key)

def validate_token(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    token = credentials.credentials
    print(f"Validating token: {token}", flush=True)  # Debugging line to check the token
    try:
        public_key = get_public_key()
        payload = jwt.decode(token, public_key, algorithms=["RS256"], audience="account")
        return payload
    except Exception:
        raise HTTPException(status_code=401, detail="Token inv�lido")