import argparse
from recorder import record_audio, find_device_id
from transcriber import transcribe_audio  

def handle_record(args):
    filename = args.audio_file
    duration = args.duration
    samplerate = args.samplerate
    device_name_substring = args.device_name_substring
    device_id = args.device_id if args.device_id is not None else find_device_id(device_name_substring)
    record_audio(filename, duration, samplerate, device_id)

def handle_transcribe(args):
    transcribe_audio(args.audio_file, args.transcript_output)


def main():
    parser = argparse.ArgumentParser(description='Record or transcribe audio.')
    parser.add_argument('--action', type=str, choices=['record', 'transcribe'], required=True, help='Action to perform: record or transcribe')
    parser.add_argument('-i', '--audio_file', type=str, default="files/record.wav", help='The name of the recorded audio file.')
    parser.add_argument('-o', '--transcript_output', type=str, default="files/transcript.txt", help='The name of the output transcript file.')
    parser.add_argument('-d', '--duration', type=float, default=10, help='The duration of the recording in seconds.')
    parser.add_argument('-r', '--samplerate', type=int, default=48000, help='The samplerate of the recording in Hz.')
    parser.add_argument('-n', '--device_name_substring', type=str, default="EchoCardsInput", help='The substring to search for in the device name.')
    parser.add_argument('-id', '--device_id', type=int, default=None, help='The device ID to use for recording. Will look automatically for "EchoCardsInput" if not specified.')
    
    args = parser.parse_args()

    action_handlers = {
        'record': handle_record,
        'transcribe': handle_transcribe
    }

    action_handlers[args.action](args)

if __name__ == '__main__':
    main()

