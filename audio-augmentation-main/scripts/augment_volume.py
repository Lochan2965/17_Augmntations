from pydub import AudioSegment
import os

def adjust_volume(audio_file, volume_change=5, output_path='.'):
    sound = AudioSegment.from_file(audio_file)
    new_sound = sound + volume_change 
    
    base_name = os.path.basename(audio_file)
    output_file = os.path.join(output_path, f'volume_adjusted_{volume_change}_{base_name}')
    new_sound.export(output_file, format="wav")
    print(f'Saved: {output_file}')

def batch_adjust_volume(input_folder, output_folder, volume_change=5):
    os.makedirs(output_folder, exist_ok=True)
    for audio_file in os.listdir(input_folder):
        if audio_file.endswith('.wav'):
            adjust_volume(os.path.join(input_folder, audio_file), volume_change, output_folder)

if __name__ == '__main__':
    batch_adjust_volume('../recordings', '../augmented/volume_adjusted', 5) 
