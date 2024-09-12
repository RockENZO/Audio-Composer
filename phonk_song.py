import numpy as np
from pydub import AudioSegment
from pydub.playback import play
from pydub.effects import normalize, compress_dynamic_range
import random

# Custom function to generate a sine wave sound using numpy
def generate_sine_wave(frequency, duration, sample_rate=44100, amplitude=0.5):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = amplitude * np.sin(2 * np.pi * frequency * t)
    return np.int16(wave * 32767)  # Convert to 16-bit PCM

# Custom function to convert numpy array to AudioSegment
def numpy_to_audiosegment(wave, sample_rate=44100):
    return AudioSegment(
        wave.tobytes(),
        frame_rate=sample_rate,
        sample_width=2,  # 16-bit audio
        channels=1       # Mono sound
    )

# Improved distortion function
def apply_distortion(sound, gain=20, mix=0.8):
    """Apply heavy distortion with mix control"""
    distorted = sound.compress_dynamic_range(threshold=-15, ratio=6.0, attack=2.0, release=10.0)
    distorted = distorted + gain
    return sound.overlay(distorted, gain_during_overlay=mix)

# Load drum samples (provide the correct paths to your samples)
kick_sample = AudioSegment.from_wav("kick.wav")
snare_sample = AudioSegment.from_wav("snare.wav")
hihat_sample = AudioSegment.from_wav("hihat.wav")
clap_sample = AudioSegment.from_wav("clap.wav")
cowbell_sample = AudioSegment.from_wav("cowbell.wav")  # New sample for phonk style

# Create a more authentic phonk bassline
def create_phonk_bassline():
    # Phonk often uses minor scales and repetitive, hypnotic patterns
    base_freq = 55  # A1 note
    minor_scale = [0, 3, 5, 7, 10, 12]  # Minor scale intervals
    
    bassline = AudioSegment.silent(duration=0)
    pattern = [0, 0, 5, 3, 0, 0, 7, 5]  # Example phonk-style pattern
    
    for interval in pattern:
        freq = base_freq * (2 ** (interval / 12))
        bass_wave = generate_sine_wave(frequency=freq, duration=0.125)  # 125ms per note for that quick, bouncy feel
        bass = numpy_to_audiosegment(bass_wave)
        bass = bass + 10  # Increase bass volume
        bass = apply_distortion(bass, gain=25, mix=0.9)  # Heavy distortion
        bassline += bass
    
    return normalize(bassline)

# Function to create an authentic phonk drum pattern
def create_phonk_drum_pattern():
    pattern = AudioSegment.silent(duration=0)
    beat_duration = 125  # 125ms per beat (120 BPM, typical for phonk)

    for i in range(16):  # 16-beat pattern for more complexity
        current = AudioSegment.silent(duration=beat_duration)
        
        # Kick on every 4th beat
        if i % 4 == 0:
            current = current.overlay(kick_sample)
        
        # Snare on every 4th beat, offset by 2
        if (i + 2) % 4 == 0:
            current = current.overlay(snare_sample)
        
        # Hi-hat on every beat, alternating between open and closed
        if i % 2 == 0:
            current = current.overlay(hihat_sample)
        else:
            current = current.overlay(hihat_sample - 3)  # Slightly quieter for variation
        
        # Clap every 8 beats
        if i % 8 == 4:
            current = current.overlay(clap_sample)
        
        # Cowbell occasionally for that phonk flavor
        if i in [7, 15]:
            current = current.overlay(cowbell_sample - 5)
        
        pattern += current

    return pattern

# Function to combine bass and drum pattern into a phonk loop
def create_phonk_loop():
    bassline = create_phonk_bassline()
    drum_pattern = create_phonk_drum_pattern()
    
    # Layer the bassline and drum pattern with slight offset for groove
    phonk_loop = bassline.overlay(drum_pattern, position=20)
    return phonk_loop

# Create a full phonk track with structure
def create_phonk_track():
    intro = create_phonk_drum_pattern() * 2
    
    main_loop = create_phonk_loop() * 4
    
    # Create variation by removing bass occasionally
    variation = create_phonk_drum_pattern() * 2 + create_phonk_loop() * 2
    
    bridge = (create_phonk_bassline() * 4).overlay(create_phonk_drum_pattern() * 2)
    
    outro = create_phonk_loop() * 2 + create_phonk_drum_pattern()

    # Combine all parts with crossfades
    phonk_track = (
        intro.append(main_loop, crossfade=250)
        .append(variation, crossfade=250)
        .append(bridge, crossfade=250)
        .append(main_loop, crossfade=250)
        .append(outro, crossfade=500)
    )

    # Apply overall effects for that phonk sound
    phonk_track = compress_dynamic_range(phonk_track, threshold=-10, ratio=4.0, attack=5.0, release=50.0)
    phonk_track = normalize(phonk_track)

    return phonk_track

# Generate and play the authentic phonk track
authentic_phonk_track = create_phonk_track()
play(authentic_phonk_track)

# Export the track to a wav file
authentic_phonk_track.export("authentic_phonk_track.wav", format="wav")