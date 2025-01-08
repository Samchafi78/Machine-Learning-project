# Machine-Learning-project
Projet de machine learning sur la prédiction de maladie cardiaque chez des patients

# 1) Instructions pour exécuter le projet en CLI

Clonez le repository :
$ git clone https://github.com/Samchafi78/Machine-Learning-project.git

Accédez à votre dossier cloné:
$ cd Projet_machine_learning

Exécuter jupyter-notebook:
$ jupyter-notebook

Ouvrez le fichier Projet_ML_CHAFI_Samir.ipynb et raw_merged_heart_dataset.csv
Allez dans "run" puis cliquer sur "run all Cells"

Sinon ouvrez juste le fichier .ipynb sur Git afin de voir les résultats du projet déjà obtenue précédemment


# 2) Description du Projet
Ce projet vise à prédire la présence ou l'absence de maladies cardiaques à partir d'un ensemble de données médicales. Le jeu de données utilisé contient des informations sur différents facteurs médicaux tels que l'âge, la pression artérielle, le cholestérol, et des caractéristiques catégorielles comme le type de douleur thoracique.

Le projet a été réalisé en utilisant Scikit-Learn pour le traitement des données, la création de pipelines, et l'entraînement de différents modèles de machine learning.

# 3) Objectif du Projet
L'objectif principal est de créer un modèle fiable capable de prédire la présence d'une maladie cardiaque. Plusieurs modèles ont été testés pour comparer leurs performances:

- Régression Logistique
- Arbre de Décision
- Forêt Aléatoire
- Extra Trees Classifier
- Dummy Classifier (modèle aléatoire)
- --> Meilleur modèle : Extra Trees Classifier avec une précision de 0.96


# 4) Jeu de Données
Le jeu de données contient 13 caractéristiques et une colonne cible appelée "target", indiquant la présence (1) ou l'absence (0) d'une maladie cardiaque.

Caractéristiques principales :
- age : Âge de la personne
- sex : Sexe (1 = Homme, 0 = Femme)
- cp : Type de douleur thoracique
- trestbps : Pression artérielle au repos
- chol : Cholestérol sérique
- fbs : Glycémie à jeun
- restecg : Résultat de l'électrocardiogramme au repos
- thalachh : Fréquence cardiaque maximale atteinte
- exang : Angine induite par l'effort
- oldpeak : Dépression ST
- slope : Pente du segment ST
- ca : Nombre de vaisseaux principaux colorés par fluoroscopie
- thal : Résultat du test Thalassemie



CHAFI RAHAMATTOULLA Samir
