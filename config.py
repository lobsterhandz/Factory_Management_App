class Config:
    # Database Configuration
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Laserface2024$@localhost/factory_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Secret Key for Sessions
    SECRET_KEY = 'your_secret_key_here'

    # Flask-Limiter Settings
    RATELIMIT_STORAGE_URL = 'memory://'
    RATELIMIT_DEFAULT = "200 per day;50 per hour"

    # Debugging and Development
    DEBUG = True
    TESTING = False

    # JSON Settings
    JSON_SORT_KEYS = False
