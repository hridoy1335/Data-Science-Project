import os, logging, sys
from datetime import datetime


FILE_DIR = 'logs'
FILE_DIR = os.path.join(os.getcwd(),FILE_DIR)

os.makedirs(FILE_DIR,exist_ok=True)

CURRENT_TIME = datetime.now().strftime("%Y-%m-%d-%H:%M")
FILE_NAME = f"log_{CURRENT_TIME}.log"

LOG_FILE = os.path.join(FILE_DIR,FILE_NAME)

logging.basicConfig(
    format='%(asctime)s - %(module)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger('test')