import streamlit as st
from multiapp import MultiApp
from apps import home, data, model,eda # import your app modules here

app = MultiApp()

st.markdown("""
# Sentiment Analysis on Product Review Dataset

Given a user review of a particular product and doing a sentiment classification on the review.
Sentiment classification aims to determine the overall intention of a written text which can be of admiration or criticism type.
 


""")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Data", data.app)
app.add_app("Model", model.app)
app.add_app("EDA", eda.app)
# The main app
app.run()
