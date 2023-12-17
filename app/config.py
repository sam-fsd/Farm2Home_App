from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    A class representing the settings for the application.

    Attributes:
        database_hostname (str): The hostname of the database.
        database_port (str): The port number of the database.
        database_password (str): The password for the database.
        database_name (str): The name of the database.
        database_username (str): The username for the database.
        secret_key (str): The secret key for the application.
        algorithm (str): The algorithm used for encryption.
        access_token_expire_minutes (int): The expiration time for access tokens in minutes.

    Config:
        env_file (str): The path to the environment file to load the settings from.
    """

    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"


settings = Settings()
