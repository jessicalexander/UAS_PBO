import logging
import os
from functools import wraps

current_dir = os.path.dirname(os.path.abspath(__file__))
logfile_path = os.path.join(current_dir, 'db', 'backlog.txt')
logging.basicConfig(filename=logfile_path, level=logging.INFO, format='%(asctime)s - %(message)s')

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Extract the username from the first argument
        username = args[0]._name if args else 'Unknown'
        logging.info(f'{func.__name__} was called by {username}.')
        return func(*args, **kwargs)
    return wrapper
