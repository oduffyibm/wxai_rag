from dotenv import load_dotenv, find_dotenv
import os

load_dotenv()

print(os.getenv('api_key'))