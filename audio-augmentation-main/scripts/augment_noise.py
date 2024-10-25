from pydub import AudioSegment
from pydub.generators import Sine
import os


def add_noise(input_file, noise_level, output_folder):
    # Load the input audio
    sound = AudioSegment.from_file(input_file)

    # Generate a sine wave as noise
    noise = Sine(440).to_audio_segment(duration=len(sound))  # Match the duration

    # Adjust the gain of the noise
    noise = noise.apply_gain(noise_level)

    # Combine the original sound with noise
    noisy_sound = sound.overlay(noise)

    # Save the output
    output_file = os.path.join(output_folder, os.path.basename(input_file))
    noisy_sound.export(output_file, format="wav")


def batch_add_noise(input_folder, output_folder, noise_level):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for audio_file in os.listdir(input_folder):
        if audio_file.endswith(".wav"):
            add_noise(os.path.join(input_folder, audio_file), noise_level, output_folder)


if __name__ == '__main__':
    input_folder = '../recordings'  # Adjust this path as necessary
    output_folder = '../augmented/noise'  # Adjusted path for output
    batch_add_noise(input_folder, output_folder, noise_level=-20)  # Set your desired noise level
