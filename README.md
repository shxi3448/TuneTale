# 🎶 TuneTale: Song Recommender using Audio Features 
<!--TuneTale is an ML model that trains on a dataset of 114,000 Spotify tracks, learning features of each song, then -->
### Nathan So and Sharon Xiang - CSCI 4622

## *Problem*
With millions of songs on Spotify, it's hard for users to discover music outside of the genres they already listen to. Traditional recommender systems rely on listening history, which means they rarely surface songs from unfamiliar genres. We want to fix this by allowing users to plug in any song, even ones outside of their typical genres, and find more songs that sound just like it. 

## *Plan*
We plan to use Spotify datasets from Kaggle that contain thousands of tracks, each labeled with audio features such as danceability, energy, and loudness. After normalizing these features to a common scale, we use K-Nearest Neighbors to find the songs closest to a given track in feature space and return them as recommendations.

## *Dataset*
The dataset we plan to use has 114,000 tracks from 114 different genres from Spotify's API. Here is the link: 

[Spotify Tracks Dataset | Audio Features](https://www.kaggle.com/datasets/saichaitanyareddyai/spotify-tracks-dataset-audio-features)


## *Setup & Running the Dataset Download*

### Prerequisites
1. **Get a Kaggle API Token:**
   - Go to https://www.kaggle.com/settings/account
   - Click "Create New API Token" (downloads `kaggle.json`)
   - Copy the token value

2. **Create `.env` file** in the project root:
   ```
   export KAGGLE_API_TOKEN=YOUR_TOKEN_HERE
   ```
   Replace `YOUR_TOKEN_HERE` with the token from step 1.

### Running the Script

1. **Activate the virtual environment:**
   ```bash
   source .venv/bin/activate
   ```

2. **Load the API token and run the download:**
   ```bash
   source .env && python download_dataset.py
   ```

   This will download the Spotify dataset (~7.9MB) to your local cache. On subsequent runs, it will use the cached version (no re-download).

3. **The dataset path will be printed:**
   ```
   Path to dataset files: /Users/YOUR_USERNAME/.cache/kagglehub/datasets/saichaitanyareddyai/spotify-tracks-dataset-audio-features/versions/1
   ```

**Note:** The `.env` file is gitignored for security. Don't commit your API token!

