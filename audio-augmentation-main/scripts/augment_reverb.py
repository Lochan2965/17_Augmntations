from pydub import AudioSegment
import os

def add_reverb(input_file, output_folder):
    sound = AudioSegment.from_file(input_file)
    reverb = sound + sound - 10  # Simple reverb effect
    output_file = os.path.join(output_folder, os.path.basename(input_file))
    reverb.export(output_file, format="wav")

def batch_add_reverb(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for audio_file in os.listdir(input_folder):
        if audio_file.endswith(".wav"):
            add_reverb(os.path.join(input_folder, audio_file), output_folder)

if __name__ == '__main__':
    input_folder = '../recordings'  # Adjust this path as necessary
    output_folder = '../augmented/reverbed'  # Adjusted path for output
    batch_add_reverb(input_folder, output_folder)
