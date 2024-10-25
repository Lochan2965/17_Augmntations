import os
from scripts.augment_pitch import batch_pitch_shift
from scripts.augment_speed import batch_change_speed
from scripts.augment_volume import batch_adjust_volume
from scripts.augment_time_shift import batch_time_shift
from scripts.augment_filter import batch_filter_audio
from scripts.augment_echo import batch_add_echo
from scripts.augment_frequency_shift import batch_frequency_shift
from scripts.augment_noise import batch_add_noise
from scripts.augment_rir import batch_apply_rir
from scripts.augment_formant_shift import batch_formant_shift
from scripts.augment_reverb import batch_add_reverb
from scripts.augment_stereo_panning import batch_pan_audio
from scripts.augment_harmonic_distortion import batch_add_harmonic_distortion
from scripts.augment_dynamic_compression import batch_compress_audio
from scripts.augment_spectral_masking import batch_spectral_masking
from scripts.augment_pitch_contouring import batch_pitch_contouring


def run_augmentations():
    recordings_folder = 'recordings'
    augmented_folder = 'augmented'

    # Existing augmentations
    batch_pitch_shift(recordings_folder, os.path.join(augmented_folder, 'pitch_shifted'), 2)
    batch_change_speed(recordings_folder, os.path.join(augmented_folder, 'speed_variation'), 1.5)
    batch_adjust_volume(recordings_folder, os.path.join(augmented_folder, 'volume_adjusted'), 5)
    batch_time_shift(recordings_folder, os.path.join(augmented_folder, 'time_shifted'), 300)
    batch_filter_audio(recordings_folder, os.path.join(augmented_folder, 'filtered'), 5000)
    batch_add_echo(recordings_folder, os.path.join(augmented_folder, 'echoed'), 150)
    batch_frequency_shift(recordings_folder, os.path.join(augmented_folder, 'frequency_shifted'), 1.2)

    # New augmentations
    batch_add_noise(recordings_folder, os.path.join(augmented_folder, 'noisy'), -20)
    batch_apply_rir(recordings_folder, os.path.join(augmented_folder, 'rir_applied'), './rir_sample.wav')
    batch_formant_shift(recordings_folder, os.path.join(augmented_folder, 'formant_shifted'), 2)
    batch_add_reverb(recordings_folder, os.path.join(augmented_folder, 'reverb_applied'))
    batch_pan_audio(recordings_folder, os.path.join(augmented_folder, 'panned'), 0.5)  # Example pan value
    batch_add_harmonic_distortion(recordings_folder, os.path.join(augmented_folder, 'distorted'))
    batch_compress_audio(recordings_folder, os.path.join(augmented_folder, 'compressed'))
    batch_spectral_masking(recordings_folder, os.path.join(augmented_folder, 'masked'), 22050)  # Sample rate
    batch_pitch_contouring(recordings_folder, os.path.join(augmented_folder, 'contoured'), [0.5, -0.5, 1.0])


if __name__ == '__main__':
    run_augmentations()

