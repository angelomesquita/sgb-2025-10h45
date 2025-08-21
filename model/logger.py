import logging
import os

# logs path
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# basic config
logging.basicConfig(
    filename=os.path.join(LOG_DIR, "app.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

# loggers
app_logger = logging.getLogger("App")
employee_logger = logging.getLogger("Employee")
auth_logger = logging.getLogger("Auth")
