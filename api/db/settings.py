from pydantic import BaseSettings




class Settings(BaseSettings):

    """
    Хранит в себе данные настроек с валидацией 
    Pydantic
    """
    postgres_db:str = None
    postgres_user:str = None
    postgres_password:str = None
    secret:str = None
    mail_username:str = None
    mail_password:str = None
    

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings: Settings = Settings()