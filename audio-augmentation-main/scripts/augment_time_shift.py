from pydub import AudioSegment
import random
import os

def time_shift(audio_file, shift_ms=500, output_path='.'):
    sound = AudioSegment.from_file(audio_file)
    shift_amount = random.randint(-shift_ms, shift_ms)
    
    if shift_amount > 0:
        new_sound = AudioSegment.silent(duration=shift_amount) + sound
    else:
        new_sound = sound[-shift_amount:]
    
    base_name = os.path.basename(audio_file)
    output_file = os.path.join(output_path, f'time_shifted_{shift_amount}_{base_name}')
    new_sound.export(output_file, format="wav")
    print(f'Saved: {output_file}')

def batch_time_shift(input_folder, output_folder, shift_ms=500):
    os.makedirs(output_folder, exist_ok=True)
    for audio_file in os.listdir(input_folder):
        if audio_file.endswith('.wav'):
            time_shift(os.path.join(input_folder, audio_file), shift_ms, output_folder)

if __name__ == '__main__':
    batch_time_shift('../recordings', '../augmented/time_shifted', 500)  
