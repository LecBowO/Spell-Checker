import streamlit as st
from spellchecker import SpellChecker

st.set_page_config(page_title='SPELL | CHECKER', page_icon='favicon.png')

spell = SpellChecker()

def correct_spell(word):
    return spell.correction(word)

st.write("# Word Corrector")

word = st.text_input("Enter a word")

if st.button("Predict"):
    corrected_spell = correct_spell(word).capitalize()
    st.write(f"## {corrected_spell}")