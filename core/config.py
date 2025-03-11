import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME: str = "FastAPI PostgreSQL App"
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "defaultsecret")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60  # 1 hour

    DEBUG: bool
    CURRENT_VERSION: str
    ANDROID_APP_VERSION: str

    # MySQL Database
    MYSQL_HOST: str
    MYSQL_PORT: int
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_DBNAME: str

    # MongoDB
    MONGODB_HOST: str
    MONGODB_PORT: int
    MONGODB_USER: str
    MONGODB_PASSWORD: str
    MONGODB_DBNAME: str

    # Security
    JWT_SECRET: str

    # Google Cloud Storage
    GOOGLE_APPLICATION_CREDENTIALS: str
    GCS_BUCKET_NAME: str

    # SMTP Configuration
    SMTP_USER: str
    SMTP_PASSWORD: str
    SMTP_SERVER: str
    SMTP_PORT: int

    # Firebase
    FIREBASE_API_KEY: str

    # FTP
    FTP_IP: str
    FTP_USER: str
    FTP_PASSWORD: str
    FTP_PATH: str

    class Config:
        env_file = ".env"


settings = Settings()
