## Machine Learning Music Genre Classifier Project

This model was trained with a dataset of over 200,000 songs from Spotify, 24 genres, and 15 audio analysis features (ex. acousticness, danceability, energy, loudness). A song search leads to a Spotify API call to retrive audio analysis features along with the artist's actual genre and the song's mini-player ID to update the page. The audio analysis features are used as input to the ML model to output the predicted genre with a confidence percentage.

![alt text](https://cdn-images-1.medium.com/max/2400/1*pVJM5_JAVW4GsurMwx0vwg.png)

## Highlights
Data Exploration: 232k songs from Spotify with 26 genres + 15 audio analysis features                                                          
26 genres of songs classified by Spotify     
R&B, Hip-Hop, Soul, Electronic etc    
Data preparation: remove irrelevant genres, change data type, and append additional columns.   
Baseline distribution: soundtrack - 4.6%, Indie - 4.5%   
More feature is better - 15 features leveraged   
After appending additional features, the model improves from 29.8% to 32.4%  
Removing binary feature works better 
Accuracy without “Explicit”: 34.569%  Accuracy with “Explicit”: 34.356% 
Binary function made Random Forest less accurate 
We kept the “Explicit” feature 
Training the model - hyperparameter tuning: sweetspot for n_estimator and max_depth 
Final trained model accuracy: 34.356% 

