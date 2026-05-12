import logging
import os
from datetime import datetime


def configurer_logger():
    """Configure et retourne le logger global du projet."""

    logs_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
    os.makedirs(logs_dir, exist_ok=True)

    nom_fichier = datetime.now().strftime("tp3_%Y-%m-%d_%H-%M-%S.log")
    chemin_log  = os.path.join(logs_dir, nom_fichier)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s  [%(levelname)s]  %(name)s — %(message)s",
        datefmt="%H:%M:%S",
        handlers=[
            logging.FileHandler(chemin_log, encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )

    logger = logging.getLogger("TP3")
    logger.info(f"Logger initialise — fichier : {chemin_log}")
    return logger
