from fastapi_users.authentication import CookieTransport, JWTStrategy, AuthenticationBackend

from config import settings

cookie_transport = CookieTransport(cookie_max_age=3600)

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=settings.jwt_secret_key, 
        lifetime_seconds=settings.jwt_lifetime_sec
    )

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy
)
