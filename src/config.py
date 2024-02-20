from pydantic_settings import BaseSettings


class _Settings(BaseSettings):

    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_NAME: str = "name"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: str | int = "5432"

    @property
    def url(self) -> str:
        _format = "postgresql+asyncpg://{user}:{password}@{host}:{port}/{name}"
        return _format.format(
            user=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_HOST,
            port=self.POSTGRES_PORT,
            name=self.POSTGRES_NAME,
        )


SETTINGS = _Settings()
