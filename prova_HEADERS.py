import requests
import streamlit as st

# Creazione della sessione
session = requests.Session()

# Esegui una richiesta GET a httpbin.org per vedere quali header vengono inviati
if st.button('premi'):
  response = session.get("https://httpbin.org/headers")
  st.write(response.json())
  print("Header inviati (default):", response.json())
