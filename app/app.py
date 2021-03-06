import streamlit as st
import numpy as np 
import pandas as pd
import tensorflow as tf
from tensorflow import keras
#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
from PIL import Image
from classify import photo_tester
#from io import BytesIO, StringIO

#---------origianl app file-----------#


# model = tf.keras.models.load_model('./Data/my_model') # saved from colab
# df = pd.read_csv('./Data/recipie_df.csv') # dataframe of recipies and ingredients



# uploaded_file = st.file_uploader("Choose an image...", type=['jpg','png', 'jpeg'])
# if uploaded_file is not None:
#     image = Image.open(uploaded_file)
#     img = uploaded_file.getvalue()
#     st.image(image, caption='Uploaded Image.', use_column_width=True)
#     st.write("")
#     st.write("Classifying...")
#     classification = photo_tester(image)




#------------new app file------------#
# '''
# MICHAEL FIX LATER - copying new app.py file from local version, includes formatting, sidebar, listing
# of cockatils, github link etc. keeping old format in case it does not display properly on streamlit sharing
# '''



# title and header 
st.title('Cocktail Classifier Beta V 0.2')
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

# contact info for bottom of sidebar
st.sidebar.info('Michael\'s: [Github](https://github.com/MichaelHarnett?tab=repositories)  and  [LinkedIn](https://www.linkedin.com/in/michael-c-harnett/)')





model = tf.keras.models.load_model('./Data/my_model') # saved from colab
df = pd.read_csv('./Data/recipie_df.csv') # dataframe of recipies and ingredients





uploaded_file = st.file_uploader("Show me your drinks!", type=['jpg','png', 'jpeg'])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img = uploaded_file.getvalue()
    st.image(image, caption='Looks delicious! I\'m jealous!', use_column_width=True)
    #st.write("")
    st.spinner('Hmmmmmmmmm, tasty, tasty....but what is it?') # found code online to display text while the app is thinking, testing it out
    
    classification = photo_tester(image)
    
    
    
    
st.info('This app was created as a deep learning, nerual network projcet for Metis. Something isn\'t working right? Want to see your favorite drink on here? Having a bad day and just want to vent? Let me know! I\'m actively working on imporving this app! Contact info is available at the bottom of the sidebar to your left!') 