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


model = tf.keras.models.load_model('./Data/my_model') # saved from colab
df = pd.read_csv('app_data/recipie_df.csv') # dataframe of recipies and ingredients



uploaded_file = st.file_uploader("Choose an image...", type=['jpg','png', 'jpeg'])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img = uploaded_file.getvalue()
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    classification = photo_tester(image)