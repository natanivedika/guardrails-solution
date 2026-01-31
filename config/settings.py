
class Settings:
    """
    Application-wide configuration settings. 

    Holds all environment-specific constants used across the app,
    including database connectivity, vector store paths, NLP model selection,
    and similarity matching thresholds.
    """
    

    DB_DSN: str = "postgresql://postgres:postgres@localhost:5432/postgres"
    CHROMA_PATH: str = "./chroma"
    SPACY_MODEL: str = "en_core_web_sm"
    VECTOR_SIM_THRESHOLD: float = 0.85
