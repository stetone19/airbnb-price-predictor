import streamlit as st
import pandas as pd
import joblib

# 1. Carica il modello e le colonne salvate
model = joblib.load('random_forest_airbnb.pkl')
model_columns = joblib.load('model_columns.pkl')

# 2. Dizionario con le coordinate dei quartieri principali di Milano
quartieri_milano = {
    "Centro Storico (Duomo)": {"lat": 45.4642, "lon": 9.1900},
    "Navigli / Ticinese": {"lat": 45.4522, "lon": 9.1726},
    "Brera / Moscova": {"lat": 45.4721, "lon": 9.1866},
    "Isola / Porta Garibaldi": {"lat": 45.4872, "lon": 9.1884},
    "Città Studi / Porta Venezia": {"lat": 45.4789, "lon": 9.2285},
    "Porta Romana": {"lat": 45.4519, "lon": 9.2023},
    "City Life / Fiera": {"lat": 45.4776, "lon": 9.1556},
    "San Siro": {"lat": 45.4780, "lon": 9.1240},
    "Bicocca": {"lat": 45.5139, "lon": 9.2106}
}

# 2. Intestazione della Web App
st.set_page_config(page_title="Airbnb Predictor", page_icon="⛪")
st.title('⛪ Milan AirBnb Price Predictor')
st.markdown("Use the sliders below to set the accommodation features and discover the predicted price")

# 3. Creiamo i controlli per l'utente (Slider e menu a tendina)
col1, col2 = st.columns(2)

with col1:
    # I cursori ora sono collegati a cascata!
    bedrooms = st.slider('Stanze da letto', 1, 5, 1)
    # Il numero minimo di letti sarà pari al numero di stanze
    beds = st.slider('Letti', min_value=bedrooms, max_value=10, value=bedrooms)
    # Il numero minimo di ospiti sarà pari al numero di letti
    accommodates = st.slider('Quanti ospiti?', min_value=beds, max_value=10, value=max(2, beds))

with col2:
    rating = st.slider('Review Score (Rating)', 1.0, 5.0, 4.8, step=0.1)
    room_type = st.selectbox('Accommodation Type', ['Entire home/apt', 'Private room', 'Shared room', 'Hotel room'])
    quartiere_scelto = st.selectbox('Seleziona il quartiere:', list(quartieri_milano.keys()))

# Aggiungiamo un bottone gigante per calcolare
st.markdown("---")
if st.button('🎯 Calculate Suggested Price'):
    lat = quartieri_milano[quartiere_scelto]["lat"]
    lon = quartieri_milano[quartiere_scelto]["lon"]
    # 4. Prepariamo i dati esattamente come facevamo nel notebook
    # Usiamo coordinate medie per Milano come default per semplificare
    data = {
        'accommodates': [accommodates],
        'bedrooms': [bedrooms],
        'beds': [beds],
        'latitude': [lat],  # Ora usa la latitudine vera!
        'longitude': [lon], # Ora usa la longitudine vera
        'review_scores_rating': [rating]
    }
    
    # Gestiamo il One-Hot Encoding per il tipo di stanza
    for rt in ['Hotel room', 'Private room', 'Shared room']:
        data[f'room_type_{rt}'] = [1 if room_type == rt else 0]
        
    df_input = pd.DataFrame(data)
    df_input = df_input.reindex(columns=model_columns, fill_value=0)
    
    # 5. Facciamo la previsione!
    prediction = model.predict(df_input)[0]
    
    # 6. Mostriamo il risultato
    st.success(f"### Suggested price: {prediction:.2f} € / night")
    st.balloons() # Piccolo effetto wow!