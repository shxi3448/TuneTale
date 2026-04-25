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

---

## *Installation & Setup*

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/TuneTale.git
cd TuneTale
```

### 2. Create Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

**Required packages:**
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- jupyter

If `requirements.txt` doesn't exist, install manually:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn jupyter
```

### 4. Download the Dataset
Follow the "Setup & Running the Dataset Download" section above to get the Spotify dataset.

---

## *How to Use the Model*

### Step 1: Preprocess the Data
Run the EDA notebook to clean and normalize the data:
```bash
jupyter notebook eda.ipynb
```
- Removes duplicates (24,259 removed)
- Normalizes 9 audio features using StandardScaler
- Outputs `data/tracks_processed.csv` with 89,740 unique tracks

### Step 2: Run the KNN Model
Open and run the KNN notebook:
```bash
jupyter notebook KNNalgo.ipynb
```

### Step 3: Get Recommendations
Use the `recommend()` function:

```python
# Basic usage - search any genre
recommend("Blinding Lights", artist_name="The Weeknd")

# Genre-filtered mode - only same genre (RECOMMENDED)
recommend("Sweater Weather", artist_name="The Neighbourhood", genre_filter=True)

# Adjust number of recommendations
recommend("Bohemian Rhapsody", n=5, genre_filter=True)
```

### Parameters
- `song_name` (str): Name of the song to search for
- `artist_name` (str, optional): Artist name for disambiguation
- `n` (int): Number of recommendations (default: 10)
- `genre_filter` (bool): If True, only recommend songs from same genre (default: False)

### Example Output
```
Query: 'Sweater Weather' by The Neighbourhood [alt-rock] — genre-filtered (alt-rock)

        track_name                artists track_genre  distance
1     W.D.Y.W.F.M?      The Neighbourhood    alt-rock    0.3124
2           Broken        Seether;Amy Lee    alt-rock    0.4477
3       By the Way  Red Hot Chili Peppers    alt-rock    0.4887
```

---

## *Model Performance*

### Global Mode (No Genre Filter)
- Genre Precision@10: 16.5%
- Best for exploring different genres

### Genre-Filtered Mode ⭐ (Recommended)
- Genre Precision@10: 100%
- Best for staying within a genre
- More consistent recommendations

### Features Used
- Danceability
- Energy
- Loudness
- Valence (musical positivity)
- Tempo
- Acousticness
- Speechiness
- Instrumentalness
- Liveness

---

## *Project Structure*
```
TuneTale/
├── README.md
├── .env                        # Your Kaggle API token (gitignored)
├── download_dataset.py         # Downloads dataset from Kaggle
├── eda.ipynb                   # Data preprocessing & exploration
├── KNNalgo.ipynb              # KNN model & recommendations
├── data/
│   ├── tracks.csv             # Raw dataset (downloaded)
│   └── tracks_processed.csv   # Cleaned & normalized (generated)
└── requirements.txt           # Python dependencies
```

