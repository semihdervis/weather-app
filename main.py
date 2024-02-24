from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

# Access variables in .env
api_key = os.getenv("API_KEY")


