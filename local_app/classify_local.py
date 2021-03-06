import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import preprocessing, layers
#from keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
from PIL import Image


model = tf.keras.models.load_model('../Data/my_model') # saved from colab
df = pd.read_csv('../Data/recipie_df.csv') # dataframe of recipies and ingredients



label_names = [
 'Aperol Spritz',
 'Bloody Mary',
 'Cosmo',
 'Irish Coffee',
 'Margarita',
 'Mimosa',
 'Mojito',
 'Moscow Mule',
 'Old Fashioned',
 'Pina Colada']




def photo_tester(photo):
    '''
    This function is designed to first, pre-process the uploaded image to be commpatible with the nerual net results.
    It then predicts the top 3 classes it belongs to, and provieds a photo ingredients and how to make the highest
    probable class
    '''
    #pre-process

    #photo = image.resize((256,256,3))
    x = tf.keras.preprocessing.image.img_to_array(photo)
    x = np.expand_dims(x, axis=0)
    
    
    #argsort condensed all the probabilities into an array, from least to greatest
    backwards = model.predict(x).argsort()[0] #ascending
    forwards = []
    for items in backwards[-1::-1]:
        forwards.append(label_names[items]) #descending
        
    st.write('We believe it looks like like this!')
    st.write(forwards[0])
    
    ingredients = df.loc[df.cocktail == forwards[0]]['ingredients'].tolist()[0]
    st.write('The ingredients for this cocktail are:')
    st.write((str(ingredients)[1:-1]).replace("'",""))
    
    recipie = df.loc[df.cocktail == forwards[0]]['recipie'].tolist()[0]
    st.write('Here\'s how you make it!')
    st.write(recipie)
    
    
    st.write('Not the drink you were looking for? It could be one of these')
    st.write(forwards[1])
    st.write(forwards[2])