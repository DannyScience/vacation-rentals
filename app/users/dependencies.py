from datetime import datetime
from fastapi import Depends, HTTPException, Request
from jose import jwt, JWTError

from app.config import settings
from app.users.dao import UsersDAO
from app.users.models import Users
from app.exceptions import (
    IncorrectTokenFormat,
    TokenAbsentException,
    TokenExpiredException,
    UserIsNotPresentException,
)


def get_token(request: Request):
    token = request.cookies.get('booking_access_token')
    if not token:
        raise TokenAbsentException
    return token


async def get_current_user(token = Depends(get_token)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
    except JWTError:
        raise IncorrectTokenFormat
    expire: str = payload.get('exp')
    if (not expire) or datetime.fromtimestamp(int(expire)) < datetime.utcnow():
        raise TokenExpiredException
    user_id: str = payload.get('sub')
    if not user_id:
        raise IncorrectTokenFormat
    user = await UsersDAO.find_by_id(int(user_id))
    if not user:
        raise UserIsNotPresentException
    return user


async def get_current_admin_user(current_user: Users = Depends(get_current_user)):
    if current_user.role != 'admin':
        raise HTTPException(405, status_code='No admin permissions')
    return current_user
