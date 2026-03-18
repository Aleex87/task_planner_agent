from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Ollama
    ollama_base_url: str
    ollama_bearer_token: str

    # Model params
    model_temperature: float = 0.7
    model_top_p: float = 0.9

    # Memory
    memory_window: int = 10

    class Config:
        env_file = ".env"


settings = Settings()
