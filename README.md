# Cocktail Classifier
Deep learning and neural networks module at Metis
6/2021
<br>
<br>
For my first attempt at a Nerual Net and deep learning I wanted to do something that excites me to help psuh me through the learning curve. Natrually I leaned towards alcohol. I searched for a cocktail-themed data set far and wide, but it was nowhere to be found. My idea was to build a cocktail-classifying Convolutional Nerual Netowrk that not only tells you what you're drinking, but how you can make it for yourself. From building the data from scratch to avhieving an overall accuracy on a holdout test set of just over 70%, I would say this was a great way to dip my feet in the deep learning pool.
<br>
<br>


# Explanation of Notebooks
<hr></hr>
<b>prelim_code folder:</b>
<ul>
  <li><b>data_prelim</b> - was used to try out google_image_api, before I found out it is no longer compatible with Google.</li>
  <li><b>keras_prelim</b> - was used to begin to try and test out the synax and useage of keras. Baseline model came from this notebook</li>
  <li><b>colab_test</b> - was used to switch to using Google CoLab, was able to greatly increase speed, and layers/nodes/filters</li>
  <li><b>recipie_scraping</b> - the notebook used to scrape the cocktail recipies</li>
  <li><b>coming_together</b> - notebook used to begin to see how I can combine the predictions of my final model with the recipies scraped</li>
</ul>
<b>app folder:</b>
<ul>
  <li><b>app.py</b> - the code to run my streamlit app</li>
  <li><b>classify.py</b> - the classifer function I call in app.py</li>
  <li><b>requriements.txt</b> - requirements for streamlit social to run</li>
  <li><b>app_data folder</b> - copies of model data and recipie df to work easier in streamlit
</ul>
  
<br>
<br>


# Data
<hr></hr>
As mentioned, the data was not already collected from me. Instead, in the interest of time, and because I have been scraping for so many previous projects, I used a chrome extension to bulk grab bunches of photos of 10 different cocktails. Both Google and Bing have started limiting the total number of searches lately, so a maximum of around 800 were available per drink. I then had to manually go through every photo remove the ones that were not related, and crop some extreme backgrounds out of *some* of the photos. The result was about 4k photos left 
<br>
The recipies and ingredients were pulled from coktailDB's API

<br>
<br>


# Tools 
<hr></hr>
Google chrome Bulk Download extension was used for image captruing
Requests library was used to pull info out from an API 
Tensorflow and Keras were used for building the neural network. 
Matplotlib and Seaborn were used for visualizing the data
<br>
I also created a streamlit app that takes an input of a photo, tells you the most likely drink it is based on the probability, that drink's recipie and ingredietns,
and the next two drinks in case it's incorrect.

<br>
<br>
# Algorithms
<hr></hr>
After Trying a lot of different configurations, the final set up for the neural network was one without Transfer Learning. It has 5 Convolutional Layers, and 6 Dense Layers, Optomized with a 'softmax' into 10 categories.
<br>
<br>


# Results and Future Work
<hr></hr>
Overall I am happy with the results. The final model has a great score on the hold out test set of 70%. For the future, I would love to increase the apps potential. more cocktails, greater variety, maybe even similar drinks based on ingredients.
Aslo moving the app from streamlit to Heroku or beyond.
