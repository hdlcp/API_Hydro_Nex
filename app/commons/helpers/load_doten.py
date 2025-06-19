from pathlib import Path
import os
from dotenv import load_dotenv
from app.commons.instances.instances import logger
#from commons.instances.instances import logger 
# Chemin vers le fichier .env, compatible multi-plateformes
env_path = Path(__file__).resolve().parent.parent / 'const' / 'const' / '.env'

#logger.debug(env_path)
logger.info(env_path)
if not env_path.exists():
    raise FileNotFoundError(f"Le fichier .env est introuvable : {env_path}")


# Charger le fichier .env
env_is_load = load_dotenv(env_path)

class Dotenv:
    """Gestionnaire des variables d'environnement."""

    SMTPSERVEUR = os.getenv('smtp_server')
    SMTPPORT = int(os.getenv('smtp_port'))  # Valeur par défaut pour le port
    SMTPUSER = os.getenv('smtp_user')
    SMTPPASSWORD = os.getenv('smtp_password')
    SQLALCHEMY_DATABASE_URI = os.getenv('data_base_uri')
    GEMINI_API_KEY = os.getenv('gemini_api_key')
    COMPETITION_SECRET_KEY = os.getenv('competition_secret_key')

