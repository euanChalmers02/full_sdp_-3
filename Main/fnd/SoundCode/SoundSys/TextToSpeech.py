import pyttsx3
import librosa
import sounddevice as sd
import os

PATH = os.path.abspath(__file__)
ROOT = PATH.split("Main")
MSG_CACHE_PATH = ROOT[0] + "Main/fnd/recorded_msg"
CACHE_JSON_FILE = ROOT[0] + "Main/fnd/recorded_msg/database"

# Saves a recording of machine-spoken text to cache for quicker playback.
def save_msg_to_cache(input_text, file_name):
    if 'wav' not in file_name:
        file_name = file_name + '.wav'

    print('written to...', MSG_CACHE_PATH + "/" + file_name)
    engine = pyttsx3.init()
    engine.save_to_file(input_text, str(MSG_CACHE_PATH + "/" + file_name))
    engine.runAndWait()

# plays text-to-speech recording
def play_msg_cache(file_name):
    if '.wav' not in file_name:
        file_name = file_name + '.wav'

    [y, sr] = librosa.load(MSG_CACHE_PATH + "/" + file_name, sr=48000)
    # duration = librosa.get_duration(filename=MSG_CACHE_PATH + "/" + file_name) * 1000  # value in ms

    # simpler, and doesn't rely on timing of the recorded message
    sd.play(y, sr, blocking=True)
    # sd.sleep(int(duration))
    # sd.stop()
