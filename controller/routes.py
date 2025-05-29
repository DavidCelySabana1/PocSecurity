from fastapi import APIRouter, Depends
from facade.api_facade import get_github_user_info
from utils.token_validator import validate_token

router = APIRouter()

@router.get("/github-user/{username}")
def github_user(username: str, user=Depends(validate_token)):
    return get_github_user_info(username)