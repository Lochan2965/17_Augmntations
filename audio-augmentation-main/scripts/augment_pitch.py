from pydub import AudioSegment
import os

def pitch_shift(audio_file, semitone_change, output_path):
    sound = AudioSegment.from_file(audio_file)
    new_sound = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * (2.0 ** (semitone_change / 12.0)))
    }).set_frame_rate(sound.frame_rate)
    
    base_name = os.path.basename(audio_file)
    output_file = os.path.join(output_path, f'pitch_shifted_{semitone_change}_{base_name}')
    new_sound.export(output_file, format="wav")
    print(f'Saved: {output_file}')

# Batch processing
def batch_pitch_shift(input_folder, output_folder, semitone_change):
    os.makedirs(output_folder, exist_ok=True)
    for audio_file in os.listdir(input_folder):
        if audio_file.endswith('.wav'):
            pitch_shift(os.path.join(input_folder, audio_file), semitone_change, output_folder)

if __name__ == '__main__':
    batch_pitch_shift('../recordings', '../augmented/pitch_shifted', 2)  
