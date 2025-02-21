import streamlit as st

def app():

    if "page" not in st.session_state:
        st.session_state["page"] = "IntroFormulaireComplet"  # État par défaut

    st.title("Merci d'avoir participé au test de saisie")
