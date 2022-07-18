# (c) @sufail_sufu • @sufail_sufu

import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)


class Config(object):
    API_ID = int(os.environ.get("API_ID", "10297545"))
    API_HASH = os.environ.get("API_HASH", "9cbf97211ec3efef7ca465ff1060c50a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5431392018:AAGLco8bx0HOihd_25iuHoO_k8tEsUltkcY")
    DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
    LOGGER = logging
    OWNER_ID = int(os.environ.get("OWNER_ID", "5116267482"))
    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "0").split()))
    PRO_USERS.append(OWNER_ID)
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://arakkaldon:141481@cluster0.oa98y.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001718381245"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
