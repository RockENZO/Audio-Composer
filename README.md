# Python Audio Composer: MIDI to Piano and Phonk Track Generator

## Overview

This project is a Python-based audio processing tool that generates and manipulates music using MIDI files and audio samples. It consists of two main scripts:

1. **miditopiano.py**: Generates a piano composition from a MIDI file using pre-recorded piano samples.
2. **phonk_song.py**: Creates an authentic phonk track by generating a bassline and drum pattern using audio samples and custom sine wave generation.

## Features

- **MIDI to Piano Composition**: Convert MIDI files to piano compositions using pre-recorded samples.
- **Phonk Track Generation**: Create phonk tracks with custom basslines and drum patterns.
- **Audio Effects**: Apply normalization, compression, and distortion effects to enhance the audio output.
- **Export to WAV**: Export the generated compositions to WAV files for easy playback and sharing.

## Requirements

- Python 3.x
- numpy
- pydub
- mido

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/python-audio-composer.git
    cd python-audio-composer
    ```

2. Install the required Python packages:
    ```sh
    pip install numpy pydub mido
    ```

3. Ensure you have the necessary audio samples and MIDI files in the correct directories:
    - Place your piano samples in the `./AudioSample/` directory.
    - Place your MIDI files in the `./MIDI/` directory.

## Usage

### MIDI to Piano Composition

1. Edit the `miditopiano.py` script to specify the path to your MIDI file and the maximum duration for the composition:
    ```python
    midi_file_path = './MIDI/YourMIDIFile.mid'
    max_duration = 55  # Duration in seconds
    ```

2. Run the script:
    ```sh
    python miditopiano.py
    ```

3. The generated piano composition will be played and exported to `./output/piano_composition_truncated.wav`.

### Phonk Track Generation

1. Ensure you have the necessary drum samples in the `./AudioSample/` directory.

2. Run the `phonk_song.py` script:
    ```sh
    python phonk_song.py
    ```

3. The generated phonk track will be played and exported to `./output/authentic_phonk_track3.wav`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue to discuss any changes or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.