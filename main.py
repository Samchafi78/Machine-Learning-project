import subprocess
import sys

# Fonction pour exécuter des commandes shell
def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
        print(f" Commande réussie : {command}")
    except subprocess.CalledProcessError as e:
        print(f" Échec de la commande : {command}\n{e}")

# Étape 1 : Installation des dépendances à partir de requirements.txt
try:
    print("Installation des dépendances depuis requirements.txt...")
    run_command("pip install -r requirements.txt")
except Exception:
    print("L'installation depuis requirements.txt a échoué. Installation manuelle des packages...")

    # Étape 2 : Installation manuelle des packages si le fichier requirements.txt ne fonctionne pas
    manual_commands = [
        "sudo apt install jupyter-core",
        "pip install nbconvert",
        "pip install --upgrade jupyter nbconvert",
        "pip install pandas seaborn matplotlib",
        "pip install scikit-learn",
        "sudo apt-get install python3-tk"
    ]

    for cmd in manual_commands:
        run_command(cmd)

# Étape 3 : Conversion du Notebook en script Python
print("Conversion du fichier Notebook en script Python...")
run_command("jupyter nbconvert --to script Projet_ML_CHAFI_Samir.ipynb")

# Étape 4 : Exécution du script Python généré
print("Exécution du script Python...")
run_command("python Projet_ML_CHAFI_Samir.txt")
