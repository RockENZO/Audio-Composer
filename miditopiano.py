from pydub import AudioSegment
from pydub.playback import play
from pydub.effects import normalize
from mido import MidiFile

# Load piano samples (provide the correct paths to your samples)
piano_samples = {
    'C4': AudioSegment.from_wav('./AudioSample/C4.wav'),
    'D4': AudioSegment.from_wav('./AudioSample/D4.wav'),
    'E4': AudioSegment.from_wav('./AudioSample/E4.wav'),
    'F4': AudioSegment.from_wav('./AudioSample/F4.wav'),
    'G4': AudioSegment.from_wav('./AudioSample/G4.wav'),
    'A4': AudioSegment.from_wav('./AudioSample/A4.wav'),
    'B4': AudioSegment.from_wav('./AudioSample/B4.wav'),
    'C5': AudioSegment.from_wav('./AudioSample/C5.wav'),
    'D5': AudioSegment.from_wav('./AudioSample/D5.wav'),
    'E5': AudioSegment.from_wav('./AudioSample/E5.wav'),
    'F5': AudioSegment.from_wav('./AudioSample/F5.wav'),
    'G5': AudioSegment.from_wav('./AudioSample/G5.wav'),
    'A5': AudioSegment.from_wav('./AudioSample/A5.wav'),
    'B5': AudioSegment.from_wav('./AudioSample/B5.wav')
}

# MIDI note number to note name mapping
note_mapping = {
    60: 'C4', 61: 'C#4', 62: 'D4', 63: 'D#4', 64: 'E4', 65: 'F4', 66: 'F#4', 67: 'G4',
    68: 'G#4', 69: 'A4', 70: 'A#4', 71: 'B4', 72: 'C5', 73: 'C#5', 74: 'D5', 75: 'D#5',
    76: 'E5', 77: 'F5', 78: 'F#5', 79: 'G5', 80: 'G#5', 81: 'A5', 82: 'A#5', 83: 'B5'
}

# Function to generate a piano sound from MIDI note using samples
def generate_piano_sound(note, duration):
    if note in piano_samples:
        sound = piano_samples[note]
        # Extend or truncate the sample to match the desired note length
        if duration > len(sound) / 1000.0:  # Duration longer than sample
            num_repeats = int(duration / (len(sound) / 1000.0)) + 1
            sound = sound * num_repeats
        sound = sound[:int(duration * 1000)]  # Convert seconds to milliseconds
        return sound
    else:
        return AudioSegment.silent(duration=duration * 1000)  # If note not found, return silence

# Function to parse MIDI file and create a truncated piano song using samples
def create_piano_song(midi_file_path, max_duration):
    midi = MidiFile(midi_file_path)
    song = AudioSegment.silent(duration=0)
    total_duration = 0

    for track in midi.tracks:
        for msg in track:
            if msg.type == 'note_on':
                duration = msg.time / 1000.0  # Convert ticks to seconds (simple approximation)
                note_name = note_mapping.get(msg.note, 'C4')  # Default to 'C4' if note not found
                piano_note = generate_piano_sound(note_name, duration)
                
                # If adding this note exceeds max_duration, truncate the note duration
                if total_duration + duration > max_duration:
                    duration = max_duration - total_duration
                    piano_note = generate_piano_sound(note_name, duration)
                
                song += piano_note
                total_duration += duration
                
                # Stop if the total_duration exceeds the max_duration
                if total_duration >= max_duration:
                    return normalize(song)

    return normalize(song)

# Path to your MIDI file
midi_file_path = './MIDI/MarriedLife.mid'  # Ensure this path is correct
max_duration = 55  # Duration in seconds for the truncated song

# Generate and play the piano song
piano_song = create_piano_song(midi_file_path, max_duration)
play(piano_song)

# Export the piano song to a wav file
piano_song.export("./output/piano_composition_truncated.wav", format="wav")