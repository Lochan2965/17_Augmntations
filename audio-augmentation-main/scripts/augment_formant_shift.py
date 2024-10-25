import numpy as np
import librosa
import soundfile as sf
import os


def formant_shift(input_file, shift_factor, output_folder):
    # Load audio file
    audio, sr = librosa.load(input_file, sr=None)

    # Apply pitch shift
    shifted = librosa.effects.pitch_shift(audio, sr=sr, n_steps=shift_factor)

    # Create output path with the original file name
    base_name = os.path.splitext(os.path.basename(input_file))[0]  # Get the base file name without extension
    output_path = f"{output_folder}/{base_name}_shifted.wav"  # Add suffix for clarity

    # Save the shifted audio using soundfile
    sf.write(output_path, shifted, sr)

def batch_formant_shift(input_folder, output_folder, shift_factor):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for audio_file in os.listdir(input_folder):
        if audio_file.endswith(".wav"):
            formant_shift(os.path.join(input_folder, audio_file), shift_factor, output_folder)

if __name__ == '__main__':
    input_folder = '../recordings'  # Adjust the path as necessary
    output_folder = '../augmented/formantshift'  # Adjusted path for output
    shift_factor = 2  # You can set this to your desired shift value
    batch_formant_shift(input_folder, output_folder, shift_factor)
