from dotenv import load_dotenv
import os

load_dotenv()

AZURE_OPENAI_DEPLOYMENT_NAME: str = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "")
AZURE_OPENAI_ENDPOINT: str = os.getenv("AZURE_OPENAI_ENDPOINT", "")
AZURE_OPENAI_API_KEY: str = os.getenv("AZURE_OPENAI_API_KEY", "")

AUTH_USER_ID: str = os.getenv("AUTH_USER_ID", "")
AUTH_USER_PW: str = os.getenv("AUTH_USER_PW", "")

WEBSITES_PORT: int = int(os.getenv("WEBSITES_PORT", "8000"))
