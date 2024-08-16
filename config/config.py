import os

# Base directory of the project
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Secret key for session management and other security functions
SECRET_KEY = os.environ.get('SECRET_KEY', 'f2a9e7c9db7b4e3b9d4c87cfb845f1f8')  # Use a secure key

# Other configuration options can go here
