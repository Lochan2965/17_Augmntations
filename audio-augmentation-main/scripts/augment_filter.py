from pydub import AudioSegment
import os

def apply_high_pass_filter(input_file, cutoff_freq, output_folder):
    sound = AudioSegment.from_file(input_file)
    filtered_sound = sound.high_pass_filter(cutoff_freq)

    output_file = os.path.join(output_folder, f"highpass_{os.path.basename(input_file)}")
    filtered_sound.export(output_file, format="wav")

def apply_low_pass_filter(input_file, cutoff_freq, output_folder):
    sound = AudioSegment.from_file(input_file)
    filtered_sound = sound.low_pass_filter(cutoff_freq)

    output_file = os.path.join(output_folder, f"lowpass_{os.path.basename(input_file)}")
    filtered_sound.export(output_file, format="wav")

def batch_filter_audio(input_folder, output_folder, cutoff_freq):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for audio_file in os.listdir(input_folder):
        if audio_file.endswith(".wav"):
            apply_high_pass_filter(os.path.join(input_folder, audio_file), cutoff_freq, output_folder)
            apply_low_pass_filter(os.path.join(input_folder, audio_file), cutoff_freq, output_folder)
