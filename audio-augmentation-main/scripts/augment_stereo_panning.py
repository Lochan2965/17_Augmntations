from pydub import AudioSegment
import os

def pan_audio(input_file, pan_value, output_folder):
    sound = AudioSegment.from_file(input_file)
    panned_sound = sound.pan(pan_value)  # -1.0 (left) to 1.0 (right)
    output_file = os.path.join(output_folder, os.path.basename(input_file))
    panned_sound.export(output_file, format="wav")

def batch_pan_audio(input_folder, output_folder, pan_value):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for audio_file in os.listdir(input_folder):
        if audio_file.endswith(".wav"):
            pan_audio(os.path.join(input_folder, audio_file), pan_value, output_folder)

if __name__ == '__main__':
    input_folder = '../recordings'  # Adjust this path as necessary
    output_folder = '../augmented/stereo panned'  # Path for the panned audio
    pan_value = 0.5  # Adjust this value for desired panning (0 for center, -1 for left, 1 for right)
    batch_pan_audio(input_folder, output_folder, pan_value)
