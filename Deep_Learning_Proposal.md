# Deep Learning and Neural Networks Proposal: What's in a Drink?
Michael Harnett <br>
6/30/21
<HR></HR>

The bar can be an intimidating place! It's unlikely that you were introducted to drinking by experiencing every classic cocktail there is; Or that someone took the time to explain the difference between bourbon and whiskey (bourbon is whiskey that has at least 51% corn in the mash by the way). More often than not we try drinks we see other people ordering, or that are recommended to us by friends. But what happens if the bartender makes you a classic and you're too embarassed to ask what it is? Or you like it so much you want to make it at home? I believe I can help. The goal of this project it to create a convolutional nerual network that classisfies photos of cocktails, informing what the cocktail is. This tool would be most useful as an app available to the public, and can be further developed in any number of ways. Recipies for the drinks can also be scraped and provided, or even recommendations of similar drinks based on ingredients used. 
<br>
<br>
<br>
### Data
<hr></hr>
Unfortunately I could not find a robust data set of cocktail photos; therefore, I will have to make my own! I will utitilze the google_ images_download python package to download images myself. I plan, to start, to look at 15 cocktails, at 500 images per cocktail. This being my first deep learning project, I will start with these numbers and determine if more data points are possible. 
<br>
Recipies for drinks can be achieved from TheCocktaildb.com - a large database of cocktail recipies. 
<br>
<br>


<br>
### Algorithms
<hr></hr>
I will be using a convolutional neural network to process the images. 
<br>
<br>
<br>
### Tools
<hr></hr>
Because of the size of the data, and functionality of a neural network, I will be using a combination of Google Cloud and Google Colab for this project. <br>
Modeling will be done in Python using TensorFlow and Keras <br>
Time permitting I would like to build a streamlit app for Heroku as well.
