# job-analyzer
# Job Analyzer

Application web de **collecte et d’analyse des offres d’emploi** développée avec Python et Flask.

---

## Objectif du projet

L’objectif est de concevoir une application capable de :

* Collecter des offres d’emploi en ligne
* Stocker les données dans une base MySQL
* Analyser et visualiser les données
* Fournir une interface web interactive

---

## Technologies utilisées

* **Python** (Flask)
* **MySQL**
* **Pandas**
* **HTML / CSS**
* **JavaScript (Chart.js)**

---

## Fonctionnalités principales

   Scraping des offres d’emploi
   Stockage dans une base de données
   Affichage des offres sous forme de tableau
   Recherche par mots-clés
   Filtrage par secteur (Informatique, Ingénierie, etc.)
   Analyse des données :

* Top 5 des villes avec le plus d’offres
* Répartition des offres par secteur

  Visualisation graphique :

* Diagramme en barres (offres par ville)
* Diagramme circulaire (secteurs)

  Export des données en fichier Excel

---

## Aperçu de l'application

<img width="959" height="412" alt="image" src="https://github.com/user-attachments/assets/3e29a8bf-9e33-4af0-88bf-f09ead242dcb" />

<img width="936" height="409" alt="image" src="https://github.com/user-attachments/assets/ea5282e9-35fd-4424-9a0a-d362c85ff17c" />

---

## Structure du projet

```
job_analyzer/
│
├── app.py
├── analysis.py
├── scraper.py
├── database.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## Installation et exécution

### 1. Cloner le projet

```bash
git clone https://github.com/UlrichBryan/job-analyzer.git
cd job-analyzer
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 3. Lancer l’application

```bash
python app.py
```

### 4. Accéder à l’application

Ouvre ton navigateur sur :

```
http://127.0.0.1:5000
```

---

## Fonctionnement

1. Les données sont collectées via un script de scraping
2. Elles sont stockées dans une base MySQL
3. L’application Flask récupère ces données
4. Pandas permet de les analyser
5. Les résultats sont affichés sous forme :

   * de tableau
   * de statistiques
   * de graphiques

---

## Améliorations possibles

* Ajout de filtres avancés
* Pagination des résultats
* Dashboard interactif
* Déploiement en ligne
* Amélioration de la classification des secteurs

---

## Auteur

Projet réalisé par **Ulrich Bryan**

---

## 📜 Licence

 usage éducatif
