# Audio Augmentation

- This project generates augmented audio files from a small set of recordings to create a larger dataset.
- FFmpeg is required for processing audio files. You can install FFmpeg using Chocolatey or [Manually](https://ffmpeg.org)

## Augmentation Techniques

- Pitch Shifting: Adjusts the pitch of the audio by a specified number of semitones.
- Speed Variation: Changes the speed of the audio without altering the pitch.
- Volume Adjustment: Increases or decreases the volume of the audio.
- Time Shifting: Shifts the audio in time by adding silence or trimming the start.
- High-Pass and Low-Pass Filtering: Filters frequencies to allow only high or low frequencies to pass through.
- Echo Effect: Adds an echo to the audio to simulate reverberating environments.
- Frequency Shifting: Shifts the frequency spectrum to simulate different voice pitches.

### Installation

`choco install ffmpeg`
`pip install -r requirements.txt`
`python main.py`

### How to Use

- Place your original audio files in the recordings/ folder. Ensure the files are in WAV format.
- Run the augmentations by executing `python main.py`
- This will generate augmented files in the augmented/ folder, organized by the augmentation type.
