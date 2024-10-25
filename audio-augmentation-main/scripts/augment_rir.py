from scipy.signal import convolve
import librosa
import soundfile as sf
import os

def apply_rir(input_file, rir_file, output_folder):
    audio, sr = librosa.load(input_file, sr=None)
    rir, _ = librosa.load(rir_file, sr=sr)
    convolved_audio = convolve(audio, rir, mode='full')[:len(audio)]
    convolved_audio /= max(abs(convolved_audio))  # Normalize to avoid clipping

    output_file = os.path.join(output_folder, os.path.basename(input_file))
    sf.write(output_file, convolved_audio, sr)

def batch_apply_rir(input_folder, output_folder, rir_file):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for audio_file in os.listdir(input_folder):
        if audio_file.endswith(".wav"):
            apply_rir(os.path.join(input_folder, audio_file), rir_file, output_folder)

if __name__ == '__main__':
    input_folder = '../recordings'  # Adjust this path as necessary
    output_folder = '../augmented/rired'  # Adjusted path for output
    rir_file = '../rir_sample.wav'  # Provide the correct path to your RIR file
    batch_apply_rir(input_folder, output_folder, rir_file)
