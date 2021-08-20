import streamlit as st
import numpy as np 
import pandas as pd
import tensorflow as tf
from tensorflow import keras
#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
from PIL import Image
from classify_local import photo_tester



# title and header 
st.title('Cocktail Classifier Beta')
st.info('This application is currently being developped, and has a long way to go. It can currently only work with the'+ 
        'cocktails listed in the sidebar, but more are on the way!')



# sidebar code

st.sidebar.title('These are our currently accepted cocktails!')
st.sidebar.subheader('Margarita')
st.sidebar.subheader('Irish Coffee')
st.sidebar.subheader('Cosmopolitan')
st.sidebar.subheader('Old Fashioned')
st.sidebar.subheader('Aperol Spritz')
st.sidebar.subheader('Mojito')
st.sidebar.subheader('Pina Colada')
st.sidebar.subheader('Mimosa')
st.sidebar.subheader('Moscow Mule')
st.sidebar.subheader('Bloody Mary')

# contact info on sidebar
st.sidebar.info('Michael\'s: [Github](https://github.com/MichaelHarnett?tab=repositories)  and  [LinkedIn](https://www.linkedin.com/in/michael-c-harnett/)')


model = tf.keras.models.load_model('../Data/my_model') # saved from colab
df = pd.read_csv('../Data/recipie_df.csv') # dataframe of recipies and ingredients





uploaded_file = st.file_uploader("Show me your drinks!", type=['jpg','png', 'jpeg'])
if uploaded_file is not None:
    st.balloons()
    image = Image.open(uploaded_file)
    img = uploaded_file.getvalue()
    st.image(image, caption='Looks delicious! I\'m jealous!', use_column_width=True)
    st.spinner('Hmmmmmmmmm, tasty, tasty....but what is it?')
    classification = photo_tester(image)
    
    
    
    
st.info('This app was created as a projcet for Metis. If something isn\'t working right? Want to see your favorite drink on here? Having a bad day and just want to vent? Let me know! I\'m actively working on imporving this app! Contact info is available at the bottom of the sidebar to your left!') 