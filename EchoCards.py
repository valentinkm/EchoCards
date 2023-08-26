import argparse
from recorder import record_audio
from recorder import find_device_id

def main():
    parser = argparse.ArgumentParser(description='Record audio from a virtual audio cable.')
    parser.add_argument('-f', '--filename', type=str, default="output.wav", help='The name of the output file.')
    parser.add_argument('-d', '--duration', type=float, default=5, help='The duration of the recording in seconds.')
    parser.add_argument('-r', '--samplerate', type=int, default=48000, help='The samplerate of the recording in Hz.')
    parser.add_argument('-n', '--device_name_substring', type=str, default="EchoCardsInput", help='The substring to search for in the device name.')
    parser.add_argument('-i', '--device_id', type=int, default=None, help='The device ID to use for recording. Will look autocmaticallu for "EchoCardsInput" if not specified.')
    
    args = parser.parse_args()

    filename = args.filename
    duration = args.duration
    samplerate = args.samplerate
    device_name_substring = args.device_name_substring
    device_id = args.device_id

    if device_id is None:
        device_id = find_device_id(device_name_substring)

    record_audio(filename, duration, samplerate, device_id)

if __name__ == '__main__':
    main()




#record_audio(filename, duration, samplerate, device_id)