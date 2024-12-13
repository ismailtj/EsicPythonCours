import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import matplotlib.pyplot as plt
from datetime import datetime

# Configuration des logs
LOG_FILE = "events.log"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(message)s')

class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        logging.info(f"Modification: {event.src_path}")
        print(f"Modification: {event.src_path}")

    def on_created(self, event):
        logging.info(f"Création: {event.src_path}")
        print(f"Création: {event.src_path}")

    def on_deleted(self, event):
        logging.info(f"Suppression: {event.src_path}")
        print(f"Suppression: {event.src_path}")

def start_monitoring(path):
    """Démarre la surveillance du répertoire spécifié."""
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    
    print(f"Surveillance du répertoire : {path}")
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()

def parse_log(file_path):
    """Analyse le fichier de logs et extrait les événements."""
    events = {"time": [], "event_type": []}

    with open(file_path, "r") as file:
        for line in file:
            timestamp, event = line.split(" - ", 1)
            events["time"].append(datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S,%f"))
            events["event_type"].append(event.strip())
    
    return events

def plot_events(events):
    """Affiche un graphique des événements."""
    times = events["time"]
    event_counts = {time: times.count(time) for time in set(times)}

    plt.figure(figsize=(10, 6))
    plt.bar(event_counts.keys(), event_counts.values(), width=0.01, align='center', color='skyblue')
    plt.xlabel('Heure')
    plt.ylabel("Nombre d'événements")
    plt.title("Surveillance des modifications de fichiers")
    plt.gcf().autofmt_xdate()
    plt.show()

def main():
    print("Choisissez une option :")
    print("1. Surveiller un répertoire")
    print("2. Visualiser les événements")
    choice = input("Entrez votre choix (1 ou 2) : ")

    if choice == "1":
        path = input("Entrez le chemin du répertoire à surveiller : ")
        start_monitoring(path)
    elif choice == "2":
        events = parse_log(LOG_FILE)
        if events["time"]:
            plot_events(events)
        else:
            print("Aucun événement à afficher.")
    else:
        print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
