import secrets
"""
How to Add JWT Authentication in FastAPI
https://www.freecodecamp.org/news/how-to-add-jwt-authentication-in-fastapi/

JWT 토큰 유효시간 설정(timedelta)
https://velog.io/@devmin/JWT-token-expired-date-with-timedelta
iss: 토큰 발급자 (issuer)
sub: 토큰 제목 (subject)
aud: 토큰 대상자 (audience)
exp: 토큰의 만료시간 (expiraton), 시간은 NumericDate 형식으로 되어있어야 하며 (예: 1480849147370) 언제나 현재 시간보다 이후로 설정되어있어야합니다.
nbf: Not Before 를 의미하며, 토큰의 활성 날짜와 비슷한 개념입니다. 여기에도 NumericDate 형식으로 날짜를 지정하며, 이 날짜가 지나기 전까지는 토큰이 처리되지 않습니다.
iat: 토큰이 발급된 시간 (issued at), 이 값을 사용하여 토큰의 age 가 얼마나 되었는지 판단 할 수 있습니다.
jti: JWT의 고유 식별자로서, 주로 중복적인 처리를 방지하기 위하여 사용됩니다. 일회용 토큰에 사용하면 유용합니다.
"""
from datetime import datetime

from pydantic.schema import timedelta

from app.admin.utils import current_time, utc_seoul
from passlib.context import CryptContext
import os
from datetime import datetime, timedelta
from typing import Union, Any
import jwt
from passlib.context import CryptContext

ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days
ALGORITHM = "HS256"
# JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']     # should be kept secret
JWT_SECRET_KEY = "JWT_SECRET_KEY"
# JWT_REFRESH_SECRET_KEY = os.environ['JWT_REFRESH_SECRET_KEY']
JWT_REFRESH_SECRET_KEY = "JWT_REFRESH_SECRET_KEY"

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_hashed_password(plain_password: str) -> str:
    return password_context.hash(plain_password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    print(f" plain_password !!!!!!!!! {plain_password} \n !!!!!!!!!!\n hashed_password {hashed_password}")
    return password_context.verify(plain_password, hashed_password)

def generate_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    print(f" ######### utc_seoul is {utc_seoul()} ############ ")
    if expires_delta is not None:
        expires_delta = utc_seoul() + expires_delta
    else:
        expires_delta = utc_seoul() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt

def generate_token_by_secrets() -> str:
    return secrets.token_urlsafe(32) # python3.8 기준으로 DEFAULT_ENTROPY == 32


def refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt

def get_expiration_date() -> datetime:
    return utc_seoul() + timedelta(days=3)