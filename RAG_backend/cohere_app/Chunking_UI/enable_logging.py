from datetime import datetime
import os
import logging
def enable_logging():
    # Create the logs directory if it doesn't exist
    os.makedirs("logs", exist_ok=True)

    # Replace ":" with "-" to make it Windows-safe
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(f"logs/{current_time}_logs.log")
        ],
    )
    logger = logging.getLogger(__name__)
    return logger
logger = enable_logging()
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")