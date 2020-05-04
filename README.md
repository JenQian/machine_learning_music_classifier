## Machine Learning Music Genre Classifier Project

This model was trained with a dataset of over 200,000 songs from Spotify, 24 genres, and 15 audio analysis features (ex. acousticness, danceability, energy, loudness).  The song you input is retrieved using the Spotify API, then run through the model.


## Highlights
Data Exploration: 232k songs from Spotify with 26 genres + 15 audio analysis features  
26 genres of songs classified by Spotify
R&B, Hip-Hop, Soul, Electronic etc
Data preparation: remove irrelevant genres, change data type, and append additional columns
Baseline distribution: soundtrack - 4.6%, Indie - 4.5%
More feature is better - 15 features leveraged
After appending additional features, the model improves from 29.8% to 32.4%
Removing binary feature works better
Accuracy without “Explicit”: 34.569%  Accuracy with “Explicit”: 34.356%
Binary function made Random Forest less accurate
We kept the “Explicit” feature
Training the model - hyperparameter tuning: sweetspot for n_estimator and max_depth
Final trained model accuracy: 34.356%

