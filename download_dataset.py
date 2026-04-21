import kagglehub
import shutil
import os
from pathlib import Path

# Download latest version (cached locally after first run)
path = kagglehub.dataset_download("saichaitanyareddyai/spotify-tracks-dataset-audio-features")

print("Path to dataset files:", path)

# Create data directory if it doesn't exist
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

# Copy the dataset to data/tracks.csv
source_file = Path(path) / "spotify-tracks-dataset-detailed.csv"
dest_file = data_dir / "tracks.csv"

shutil.copy(source_file, dest_file)

print(f"✓ Dataset downloaded successfully!")
print(f"✓ Copied to: {dest_file}")
print(f"✓ Ready to use in your notebooks!")
