import numpy as np
import librosa
import soundfile as sf
import os

def pitch_contouring(input_file, contour_steps, output_folder, min_fft_size=256):
    # Load the full audio file
    audio, sr = librosa.load(input_file, sr=None)

    # Ensure the FFT size is appropriate for short segments
    fft_size = max(min_fft_size, 2 ** int(np.ceil(np.log2(len(audio)))))

    # Segment the audio (each segment with length matching FFT size)
    segmented = [audio[i:i + fft_size] for i in range(0, len(audio), fft_size)]

    # Adjust contour steps to match the number of segments
    steps = contour_steps * (len(segmented) // len(contour_steps) + 1)
    steps = steps[:len(segmented)]  # Trim to match segment count

    # Apply pitch shifting to each segment
    shifted_segments = [
        librosa.effects.pitch_shift(seg, sr=sr, n_steps=step)
        for seg, step in zip(segmented, steps)
    ]

    # Concatenate shifted segments into one audio array
    output_audio = np.concatenate(shifted_segments)

    # Generate a unique output filename based on the input filename
    base_name = os.path.basename(input_file)
    output_file_name = os.path.join(output_folder, f"contoured_{base_name}")

    # Save the output audio
    sf.write(output_file_name, output_audio, sr)

def batch_pitch_contouring(input_folder, output_folder, contour_steps):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each .wav file in the input folder
    for audio_file in os.listdir(input_folder):
        if audio_file.endswith(".wav"):
            pitch_contouring(os.path.join(input_folder, audio_file), contour_steps, output_folder)

if __name__ == '__main__':
    input_folder = '../recordings'  # Path to your input folder
    output_folder = '../augmented/contoured'  # Path to save augmented files
    contour_steps = [0.5, -0.5, 1.0]  # Define your pitch shifts
    batch_pitch_contouring(input_folder, output_folder, contour_steps)
