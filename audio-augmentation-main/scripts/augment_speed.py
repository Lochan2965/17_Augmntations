from pydub import AudioSegment
import os

def change_speed(audio_file, speed=1.0, output_path='.'):
    sound = AudioSegment.from_file(audio_file)
    new_sound = sound.speedup(playback_speed=speed)
    
    base_name = os.path.basename(audio_file)
    output_file = os.path.join(output_path, f'speed_changed_{speed}_{base_name}')
    new_sound.export(output_file, format="wav")
    print(f'Saved: {output_file}')

def batch_change_speed(input_folder, output_folder, speed=1.0):
    os.makedirs(output_folder, exist_ok=True)
    for audio_file in os.listdir(input_folder):
        if audio_file.endswith('.wav'):
            change_speed(os.path.join(input_folder, audio_file), speed, output_folder)

if __name__ == '__main__':
    batch_change_speed('../recordings', '../augmented/speed_variation', 1.1)  
