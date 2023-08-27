import sounddevice as sd
from scipy.io import wavfile

# Find the device ID for the virtual audio cable:
device_name_substring = "EchoCardsInput"
def find_device_id(device_name_substring):
    devices = sd.query_devices()
    for idx, device in enumerate(devices):
        if device_name_substring.lower() in device['name'].lower():
            return idx
    return None

# Record audio:
def record_audio(filename, duration, samplerate, device_id):
    print("Recording...")
    audio_data = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=2, dtype='int16', device=device_id, blocksize=512)
    sd.wait()  # Wait for the recording to finish
    print("Recording complete!")
    print("Audio data shape:", audio_data.shape)
    print("Audio data type:", audio_data.dtype)
    wavfile.write(filename, samplerate, audio_data)