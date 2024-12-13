# Partie 1 : Initialisation et Configuration
import os
import shutil
import logging

source_dir = input("Entrez le chemin du répertoire source : ")
if not os.path.exists(source_dir):
    raise Exception(f"Le répertoire {source_dir} n'existe pas.")

destination_dir = os.path.join(source_dir, "Classified")
os.makedirs(destination_dir, exist_ok=True)

log_file = os.path.join(destination_dir, "classification.log")
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logging.info("Démarrage du script de classification.")

# Partie 2 : Parcours et Classification des Fichiers
for file_name in os.listdir(source_dir):
    file_path = os.path.join(source_dir, file_name)

    if os.path.isdir(file_path):
        continue

    _, extension = os.path.splitext(file_name)
    extension = extension[1:].lower()

    if not extension:
        logging.warning(f"Fichier ignoré sans extension : {file_name}")
        continue

    extension_dir = os.path.join(destination_dir, extension)
    os.makedirs(extension_dir, exist_ok=True)

    destination_path = os.path.join(extension_dir, file_name)
    try:
        shutil.move(file_path, destination_path)
        logging.info(f"Déplacé : {file_path} -> {destination_path}")
    except Exception as e:
        logging.error(f"Erreur lors du déplacement de {file_path} : {e}")

# Partie 3 : Génération d'un Rapport Final
logging.info("Classification terminée.")
