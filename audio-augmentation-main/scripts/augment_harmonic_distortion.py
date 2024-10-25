from pydub import AudioSegment
import os

def add_harmonic_distortion(input_file, output_folder):
    sound = AudioSegment.from_file(input_file)
    # Adding distortion by increasing the volume
    distorted_sound = sound + 10
    output_file = os.path.join(output_folder, os.path.basename(input_file))
    distorted_sound.export(output_file, format="wav")

def batch_add_harmonic_distortion(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for audio_file in os.listdir(input_folder):
        if audio_file.endswith(".wav"):
            add_harmonic_distortion(os.path.join(input_folder, audio_file), output_folder)

if __name__ == '__main__':
    input_folder = '../recordings'  # Adjust the path as necessary
    output_folder = '../augmented/harmonic_distorted'  # Adjusted path for output
    batch_add_harmonic_distortion(input_folder, output_folder)
