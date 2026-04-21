import kagglehub

# Download latest version (cached locally after first run)
path = kagglehub.dataset_download("saichaitanyareddyai/spotify-tracks-dataset-audio-features")

print("Path to dataset files:", path)
print("Dataset downloaded successfully!")
