# Load environment variables if needed
from dotenv import load_dotenv
load_dotenv()

import os
import platform
import subprocess
from gtts import gTTS
import elevenlabs
from elevenlabs.client import ElevenLabs
from pydub import AudioSegment

# Load ElevenLabs API Key
ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")

# Function to Convert MP3 to WAV
def convert_mp3_to_wav(mp3_filepath):
    wav_filepath = mp3_filepath.replace(".mp3", ".wav")
    sound = AudioSegment.from_mp3(mp3_filepath)
    sound.export(wav_filepath, format="wav")
    return wav_filepath

# Step 1a: Setup Text to Speech–TTS–model with gTTS
def text_to_speech_with_gtts_old(input_text, output_filepath):
    language = "en"
    audioobj = gTTS(text=input_text, lang=language, slow=False)
    audioobj.save(output_filepath)

input_text = "Hi this is Ai with Jannat!"
text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")

# Step 1b: Setup Text to Speech–TTS–model with ElevenLabs
def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.generate(
        text=input_text,
        voice="Aria",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)

text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3")

# Step 2: Use Model for Text output to Voice
def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"
    audioobj = gTTS(text=input_text, lang=language, slow=False)
    audioobj.save(output_filepath)

    # Convert MP3 to WAV
    wav_filepath = convert_mp3_to_wav(output_filepath)

    # Play the WAV file
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', wav_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{wav_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', wav_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

input_text = "Hi this is Ai with Jannat autoplay testing!"
text_to_speech_with_gtts(input_text, output_filepath="output.mp3")

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.generate(
        text=input_text,
        voice="Aria",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)

    # Convert MP3 to WAV
    wav_filepath = convert_mp3_to_wav(output_filepath)

    # Play the WAV file
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', wav_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{wav_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', wav_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing_autoplay.mp3")
