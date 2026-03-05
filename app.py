import streamlit as st
import pandas as pd
import joblib

# 1. Carica il modello e le colonne salvate
model = joblib.load('random_forest_airbnb.pkl')
model_columns = joblib.load('model_columns.pkl')

# 2. Intestazione della Web App
st.set_page_config(page_title="Airbnb Predictor", page_icon="⛪")
st.title('⛪ Milan AirBnb Price Predictor')
st.markdown("Use the sliders below to set the accommodation features and discover the predicted price")

# 3. Creiamo i controlli per l'utente (Slider e menu a tendina)
col1, col2 = st.columns(2)

with col1:
    accommodates = st.slider('How many guests?', 1, 10, 2)
    bedrooms = st.slider('Bedrooms', 1, 5, 1)
    beds = st.slider('Beds', 1, 10, 1)

with col2:
    rating = st.slider('Review Score (Rating)', 1.0, 5.0, 4.8, step=0.1)
    room_type = st.selectbox('Accommodation Type', ['Entire home/apt', 'Private room', 'Shared room', 'Hotel room'])

# Aggiungiamo un bottone gigante per calcolare
st.markdown("---")
if st.button('🎯 Calculate Suggested Price'):
    
    # 4. Prepariamo i dati esattamente come facevamo nel notebook
    # Usiamo coordinate medie per Milano come default per semplificare
    data = {
        'accommodates': [accommodates],
        'bedrooms': [bedrooms],
        'beds': [beds],
        'latitude': [45.4642],  # Centro di Milano
        'longitude': [9.1900],
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