import os
from dotenv import load_dotenv

load_dotenv()

redis_config = {
    "redis_server": os.environ.get("REDIS_HOST"),
    "redis_port": os.environ.get("REDIS_PORT"),
    "redis_db": os.environ.get("REDIS_DATABASE")
}