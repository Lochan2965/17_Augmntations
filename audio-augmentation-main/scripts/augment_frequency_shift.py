from pydub import AudioSegment
import os

def frequency_shift(input_file, shift_freq, output_folder):
    sound = AudioSegment.from_file(input_file)
    shifted_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': int(sound.frame_rate * shift_freq)}).set_frame_rate(sound.frame_rate)

    output_file = os.path.join(output_folder, os.path.basename(input_file))
    shifted_sound.export(output_file, format="wav")

def batch_frequency_shift(input_folder, output_folder, shift_freq):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for audio_file in os.listdir(input_folder):
        if audio_file.endswith(".wav"):
            frequency_shift(os.path.join(input_folder, audio_file), shift_freq, output_folder)
