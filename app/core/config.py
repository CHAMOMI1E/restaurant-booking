from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_host: str = "localhost"
    db_port: str = "5432"
    db_user: str = "pg_user"
    db_password: str = "pg_password"
    db_name: str = "booking_db"
    
    @property
    def db_url(self):
        return f"asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
    
settings = Settings()