from flask_mongoengine import MongoEngine
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
import redis
import docker

db = MongoEngine()
ma = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()

client = docker.DockerClient(base_url='unix://var/run/docker.sock')
# Connect to Redis server
redis = redis.Redis(
    host='localhost', 
    port=6379,
    decode_responses=True
)

def get_mongo_engine() -> MongoEngine:
    return db
def get_redis_engine():
    return redis

def get_engine() -> docker.DockerClient:
    return client
