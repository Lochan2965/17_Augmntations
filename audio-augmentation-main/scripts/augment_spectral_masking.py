import librosa
import numpy as np
import soundfile as sf
import os

def spectral_masking(input_file, sr, time_mask=0.1, freq_mask=0.2, output_folder=None):
    audio, _ = librosa.load(input_file, sr=sr)
    spec = librosa.stft(audio)
    spec = librosa.amplitude_to_db(np.abs(spec), ref=np.max)

    # Apply time mask
    t = int(spec.shape[1] * time_mask)
    spec[:, :t] = 0

    # Apply frequency mask
    f = int(spec.shape[0] * freq_mask)
    spec[:f, :] = 0

    masked_audio = librosa.istft(librosa.db_to_amplitude(spec))

    if output_folder is not None:
        output_file = os.path.join(output_folder, os.path.basename(input_file))
        sf.write(output_file, masked_audio, sr)

def batch_spectral_masking(input_folder, output_folder, sr):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for audio_file in os.listdir(input_folder):
        if audio_file.endswith(".wav"):
            spectral_masking(os.path.join(input_folder, audio_file), sr, output_folder=output_folder)

if __name__ == '__main__':
    input_folder = '../recordings'  # Adjust this path as necessary
    output_folder = '../augmented/masked'  # Path for the masked audio
    sr = 22050  # You can adjust the sample rate if needed
    batch_spectral_masking(input_folder, output_folder, sr)
