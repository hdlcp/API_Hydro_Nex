# Créer l'application Flask
from dotenv import load_dotenv
import os
from pathlib import Path
from commons.migrations_init.migrate_app import run_migrations
from core.dependance.dependance import create_app
from data.entities.config.entities_config import db

# Charger les variables d'environnement
env_path = Path(__file__).resolve().parent / 'commons' / 'const' / 'const' / '.env'
load_dotenv(env_path)

# Créer l'application et initialiser les migrations
app, migrate = create_app()

# Créer les tables et exécuter les migrations
with app.app_context():
    try:
        # Exécuter les migrations
        run_migrations(app)
    except Exception as e:
        print(f"Erreur lors de l'initialisation de la base de données : {str(e)}")
        raise e

if __name__ == "__main__":
    # Lancer l'application
    app.run(host='0.0.0.0', port=5000, debug=True)
    