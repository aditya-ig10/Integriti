"""
Configuration Management for Integriti Platform
Handles environment variables, database connections, and service settings
"""

from pydantic_settings import BaseSettings
from typing import Optional, List
import os


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""
    
    # Application
    app_name: str = "Integriti"
    environment: str = "development"
    debug: bool = True
    secret_key: str = "your-secret-key-here-change-in-production"
    
    # API Configuration
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_workers: int = 1
    
    # Database URLs
    database_url: str = "postgresql://integriti:password@localhost:5432/integriti_dev"
    redis_url: str = "redis://localhost:6379/0"
    
    # Authentication
    jwt_secret_key: str = "your-jwt-secret-key-here"
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 30
    
    # Machine Learning
    ml_model_path: str = "./models"
    hf_home: str = "./models/huggingface"
    cuda_visible_devices: str = "0"
    
    # Graph Database
    neo4j_uri: str = "bolt://localhost:7687"
    neo4j_user: str = "neo4j"
    neo4j_password: str = "password"
    
    # Search Engine
    elasticsearch_url: str = "http://localhost:9200"
    elasticsearch_index_prefix: str = "integriti"
    
    # Message Broker
    kafka_bootstrap_servers: str = "localhost:9092"
    kafka_security_protocol: str = "PLAINTEXT"
    
    # External APIs
    openai_api_key: Optional[str] = None
    anthropic_api_key: Optional[str] = None
    
    # Social Media APIs
    twitter_bearer_token: Optional[str] = None
    facebook_access_token: Optional[str] = None
    telegram_bot_token: Optional[str] = None
    
    # Monitoring
    prometheus_port: int = 9090
    log_level: str = "INFO"
    
    # Feature Flags
    enable_attribution: bool = True
    enable_graph_analysis: bool = True
    enable_international_sharing: bool = False
    
    # CORS Settings
    allowed_origins: List[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ]
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class DatabaseSettings(BaseSettings):
    """Database-specific settings"""
    
    # PostgreSQL
    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_user: str = "integriti"
    postgres_password: str = "password"
    postgres_db: str = "integriti_dev"
    
    # Connection Pool
    pool_size: int = 10
    max_overflow: int = 20
    pool_timeout: int = 30
    pool_recycle: int = 3600
    
    @property
    def database_url(self) -> str:
        """Construct database URL from components"""
        return (
            f"postgresql://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )


class SecuritySettings(BaseSettings):
    """Security and authentication settings"""
    
    # JWT Configuration
    jwt_secret_key: str = "your-jwt-secret-key-here"
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 30
    jwt_refresh_token_expire_days: int = 7
    
    # Password Settings
    password_min_length: int = 8
    password_require_uppercase: bool = True
    password_require_lowercase: bool = True
    password_require_numbers: bool = True
    password_require_special: bool = True
    
    # Rate Limiting
    rate_limit_per_minute: int = 100
    rate_limit_burst: int = 200
    
    # CORS
    cors_origins: List[str] = [
        "http://localhost:3000",
        "https://*.integriti.ai"
    ]
    cors_methods: List[str] = ["GET", "POST", "PUT", "DELETE"]
    cors_headers: List[str] = ["*"]


class MLSettings(BaseSettings):
    """Machine Learning model settings"""
    
    # Model Paths
    model_base_path: str = "./models"
    huggingface_cache: str = "./models/huggingface"
    
    # Detection Models
    roberta_model_path: str = "models/detection/roberta"
    t5_model_path: str = "models/detection/t5"
    custom_model_path: str = "models/detection/custom"
    
    # Model Configuration
    batch_size: int = 32
    max_sequence_length: int = 512
    confidence_threshold: float = 0.9
    
    # GPU Configuration
    use_gpu: bool = True
    gpu_device_id: int = 0
    mixed_precision: bool = True
    
    # Inference Settings
    max_concurrent_requests: int = 100
    timeout_seconds: int = 30


# Global settings instances
settings = Settings()
db_settings = DatabaseSettings()
security_settings = SecuritySettings()
ml_settings = MLSettings()


def get_settings() -> Settings:
    """Get application settings"""
    return settings


def get_db_settings() -> DatabaseSettings:
    """Get database settings"""
    return db_settings


def get_security_settings() -> SecuritySettings:
    """Get security settings"""
    return security_settings


def get_ml_settings() -> MLSettings:
    """Get ML settings"""
    return ml_settings
