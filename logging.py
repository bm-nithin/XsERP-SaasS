import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(asctime)s <%(name)s.%(module)s> %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("logs/xserp.log")
    ]
)

logger = logging.getLogger("xserp")
