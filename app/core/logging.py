import logging
import logging.config
from pathlib import Path

# Ensure log directory exists
LOG_DIR = Path("./logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "application.log"

# Configure the logging settings
logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s - %(pathname)s - %(name)s - %(levelname)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    },
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "standard",
            "filename": LOG_FILE,
            "mode": "a",
            "maxBytes": 10 * 1024 * 1024,  # 10 MB
            "backupCount": 5,  # Keep 5 backups
        },
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
    },
    "loggers": {
        "": {  # Root logger
            "handlers": ["file", "console"],
            "level": "DEBUG",
            "propagate": True,
        }
    },
}

# Apply the configuration
logging.config.dictConfig(logging_config)

# Create a logger instance for use
logger = logging.getLogger("app")
