from pydub import AudioSegment
import os

def add_echo(input_file, delay_ms, output_folder):
    sound = AudioSegment.from_file(input_file)
    echo = sound - 10 
    delayed_echo = echo.overlay(sound, position=delay_ms)

    output_file = os.path.join(output_folder, os.path.basename(input_file))
    delayed_echo.export(output_file, format="wav")

def batch_add_echo(input_folder, output_folder, delay_ms):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for audio_file in os.listdir(input_folder):
        if audio_file.endswith(".wav"):
            add_echo(os.path.join(input_folder, audio_file), delay_ms, output_folder)
