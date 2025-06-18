# Ce fichier est utilisé uniquement pour l'export des modèles
# Les imports sont faits directement dans les fichiers qui en ont besoin

from data.entities.admin.admin import Admin
from data.entities.donnees.donnees import Donnees
from data.entities.dispositif.dispositif import Dispositif
from data.entities.alerte_recommandation.alerte_recommandation import Alerte_Recommandation
from data.entities.newsletter.newsletter import Newsletter

__all__ = [
    'Admin',
    'Donnees',
    'Dispositif',
    'Alerte_Recommandation',
    'Newsletter'
] 