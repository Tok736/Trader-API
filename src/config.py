from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ''' App config '''
    pythonpath: str

    db_user: str
    db_pass: str
    db_host: str
    db_port: str
    db_name: str

    jwt_secret_key:   str
    jwt_lifetime_sec: int
    auth_secret_key:  str

    redis_host: str
    redis_port: str

    mail:          str
    mail_password: str

    @property
    def sqlalchemy_url(self) -> str:
        return f"postgresql+asyncpg://{settings.db_user}:{settings.db_pass}@{settings.db_host}:{settings.db_port}/{settings.db_name}"

    class Config:
        env_file = "../.env"

settings = Settings()