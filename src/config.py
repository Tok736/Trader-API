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

    smtp_host:     str
    smtp_port:     str
    smtp_user:     str
    smtp_password: str

    sqladmin_login:      str 
    sqladmin_password:   str
    # SQLADMIN_SECRET_KEY: str

    @property
    def sqlalchemy_url(self) -> str:
        return f"postgresql+asyncpg://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"

    @property
    def redis_url(self) -> str:
        return f"redis://{self.redis_host}:{self.redis_port}"

    class Config:
        env_file = "../.env"

settings = Settings()