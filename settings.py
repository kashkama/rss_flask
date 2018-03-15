from pathlib import Path 
import os
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

SECRET_KEY = os.getenv("WEATHER_API_KEY")
print(SECRET_KEY)