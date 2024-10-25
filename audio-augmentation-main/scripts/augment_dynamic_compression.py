from pydub import AudioSegment
from pydub.effects import compress_dynamic_range
import os


def compress_audio(input_file, output_folder):
    sound = AudioSegment.from_file(input_file)
    # Apply dynamic compression
    compressed_sound = compress_dynamic_range(sound, threshold=-30.0, ratio=12.0)

    output_file = os.path.join(output_folder, os.path.basename(input_file))
    compressed_sound.export(output_file, format="wav")


def batch_compress_audio(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for audio_file in os.listdir(input_folder):
        if audio_file.endswith(".wav"):
            compress_audio(os.path.join(input_folder, audio_file), output_folder)


if __name__ == '__main__':
    input_folder = '../recordings'  # Adjust path as necessary
    output_folder = '../augmented/compressed'  # Adjusted path for output
    batch_compress_audio(input_folder, output_folder)
