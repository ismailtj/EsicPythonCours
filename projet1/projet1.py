import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Fonction pour importer un fichier de logs
def importer_logs(fichier):
    try:
        logs = pd.read_csv(fichier)
        return logs
    except Exception as e:
        print(f"Erreur: {e}")
        return None

# Fonction pour détecter les schémas suspects
def detecter_intrusions(logs):
    ip_suspectes = []

    logs['datetime'] = pd.to_datetime(logs['timestamp'])
    logs['minute'] = logs['datetime'].dt.floor('T')

    requetes_par_minute = logs.groupby(['ip', 'minute']).size().reset_index(name='nombre_requetes')

    ip_suspectes = requetes_par_minute[requetes_par_minute['nombre_requetes'] > 10]['ip'].unique()

    return ip_suspectes

# Fonction pour visualiser les données
def visualiser_donnees(logs):
    ip_counts = logs['ip'].value_counts().head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=ip_counts.values, y=ip_counts.index, palette='viridis')
    plt.title('Top 10 des adresses IP les plus fréquentes')
    plt.xlabel('Nombre de requêtes')
    plt.ylabel('Adresse IP')
    plt.show()
    if 'method' in logs.columns:
        method_counts = logs['method'].value_counts()
        plt.figure(figsize=(8, 6))
        method_counts.plot(kind='bar', color='skyblue')
        plt.title('Distribution des types de requêtes HTTP')
        plt.xlabel('Type de requête')
        plt.ylabel('Nombre de requêtes')
        plt.show()

# Fonction pour générer un rapport
def generer_rapport(ip_suspectes, fichier_sortie):
    try:
        with open(fichier_sortie, 'w') as f:
            f.write('Adresses IP suspectes:\n')
            for ip in ip_suspectes:
                f.write(f"{ip}\n")
        print(f"Rapport généré : {fichier_sortie}")
    except Exception as e:
        print(f"Erreur lors de la génération du rapport : {e}")


if __name__ == "__main__":
    fichier_logs = "C:/Users/ismai/Documents/Python cours/projet1/logs.csv"  # Remplacez par le chemin de votre fichier
    fichier_rapport = "rapport_ips_suspectes.txt"

    logs = importer_logs(fichier_logs)

    if logs is not None:
        ip_suspectes = detecter_intrusions(logs)
        print(f"IP suspectes : {ip_suspectes}")

        visualiser_donnees(logs)

        generer_rapport(ip_suspectes, fichier_rapport)
