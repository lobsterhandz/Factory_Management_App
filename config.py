import os

class Config:
    """Base configuration with default settings."""
    # General Settings
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key_here')
    DEBUG = False

    # Database Configuration
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL', 'mysql+pymysql://root:password@localhost/your_db_name'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking for performance
    SQLALCHEMY_ECHO = False  # Set to True for SQL query logs (useful for debugging)

    # Rate Limiter Settings
    RATELIMIT_DEFAULT = '200 per day;50 per hour'
    RATELIMIT_HEADERS_ENABLED = True


class DevelopmentConfig(Config):
    """Development-specific configuration."""
    DEBUG = True
    SQLALCHEMY_ECHO = True  # Enable query logging for development


class TestingConfig(Config):
    """Testing-specific configuration."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # In-memory database for tests
    SQLALCHEMY_ECHO = False


class ProductionConfig(Config):
    """Production-specific configuration."""
    DEBUG = False
    SQLALCHEMY_ECHO = False
    RATELIMIT_DEFAULT = '1000 per day;200 per hour'


# Map to environment variables
config_by_name = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
