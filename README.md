# Predicting Music Popularity

## Aim
I want to try and see if there is a link between features of a song such as tempo, key, mode,etc. and its popularity. The data is from Spotify via the API and the Youtube views from their API. I'm using Python and libraries such as sklearn. I want to find the model that has the best accuracy* of predicting whether a song is popular or not. 
*I'm using other metrics to evaluate performance

### Repository description
This is the code of my final year project for my disseration. I am trying to add inline comments along the way for ease of understanding. This is what each file is for: 
* 3yp-data-plots - A place to make plots purely on the data
* 3yp-get-data - A script to get the data from the spotify api - you input a playlist and it gets all the features for the songs in that playlist in a csv
* 3yp-automated-main - Contains the main machine learning bits, using some classifiers on the data to compare their performance
* 3yp-main-py3 - Updated automated-main to Python 3 and added GridSearch
* 3yp-feature-selection - Contains my attempts and algorithms for feature selection - WARNING: Takes a **really** long time to run

To use the code that relies on the Spotify or Youtube APIs you will need to use your own credentials. Other than that if you have all the dependencies in the imports it should work for you as well.
