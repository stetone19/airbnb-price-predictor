# 🏠 Milan Airbnb Price Predictor: Data Science Project

## 📌 Panoramica
Welcome to my Machine Learning project for predicting Airbnb listing prices in Milan.
Questo progetto analizza i dati di Airbnb per prevedere il prezzo per notte degli alloggi nella città di Milano (Italia). L'obiettivo è identificare quali fattori (posizione, dimensioni, recensioni) influenzano maggiormente il mercato e costruire un modello di Machine Learning per stimare il prezzo corretto.

## 🛠️ Tech Stack
- **Languages:** Python
- **Libraries:** Pandas, NumPy (Data Manipulation), Matplotlib, Seaborn (Visualizzazione), Scikit-Learn (Machine Learning).
- **Ambient:** VS Code, Jupyter Notebook
- **Deployment:** Streamlit Community Cloud
- **Artificial Intelligence:** Gemini Pro 

## 📊 Risultati Chiave (EDA)
- **Localization:** La vicinanza al centro è il fattore determinante (mostrato nella Heatmap geografica).
- **Tipologia:** Gli appartamenti interi hanno un premio di prezzo del X% rispetto alle stanze private.
- **Outliers:** È stata necessaria una pulizia per rimuovere annunci sopra i 500€ che falsavano la media.

## 🤖 Il Modello
Ho utilizzato un **Random Forest Regressor**.
- **Miglioramento delle performance:** Partendo da una precisione iniziale ($R^2$) di 0.17, l'integrazione di coordinate geografiche e rating ha portato il punteggio a **0.36**.
- **Errore Medio (MAE):** ~47€.

## 📊 Risultati dell'Analisi

La mappa qui sotto mostra chiaramente come i prezzi si concentrino nelle zone centrali:

![Mappa calore dei prezzi Airbnb](images/price_map.png)

Questo grafico mostra la differenza di prezzo per tipologia di alloggio

![Prezzo medio per tipo di alloggio](images/type_prices.png)

Infine ecco la matrice di correlazione fra le features

![Matrice di correlazione fra features](images/matrix.png)


