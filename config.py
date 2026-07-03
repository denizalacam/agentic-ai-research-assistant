import os

from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()

# Read the OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# Default model used throughout the project
MODEL_NAME = "gpt-5"