import os
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("AviationBot")

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def validate_api_keys():
    """Ensure necessary environment variables are set."""
    if not os.getenv("OPENAI_API_KEY"):
        logger.warning("OPENAI_API_KEY not found. Please set it in your environment variables.")
        # For demo purposes, we don't raise an error here to allow import, 
        # but the app will fail at runtime without it.