import argparse
from recorder import record_audio, find_device_id
from transcriber import transcribe_audio
from text_splitter import split_transcript, r_splitter
from text_converter import generate_qa_transcript
from anki_converter import qa2anki


def handle_record(args):
    filename = args.audio_file
    duration = args.duration
    samplerate = args.samplerate
    device_name_substring = args.device_name_substring
    device_id = args.device_id if args.device_id is not None else find_device_id(device_name_substring)
    record_audio(filename, duration, samplerate, device_id)

def handle_transcribe(args):
    transcribe_audio(args.audio_file, args.transcript_output)

def handle_transcript2anki(args):
    # Load and Split the Transcript
    transcript_file = args.transcript_file  # Assuming this is passed as an argument
    topic = args.topic
    docs = split_transcript(transcript_file)
    
    # Step 2: Convert Text to `qa_transcript`
    qa_transcript = generate_qa_transcript(docs, topic)
    
    # Step 3: Convert `qa_transcript` to Anki Importable Text File
    anki_formatted_text = qa2anki(qa_transcript)
    
    # Save it as a text file
    with open("anki_import.txt", 'w', encoding='utf-8') as f:
        f.write(anki_formatted_text)
    # write qa_transcript to markdown file
    with open("qa_transcript.md", 'w', encoding='utf-8') as f:
        f.write(qa_transcript)

    print("Transcript Q&A markdown file and anki importable text file created.")

def main():
    parser = argparse.ArgumentParser(description='Record or transcribe audio, or convert transcript to Anki.')
    
    # Common arguments
    parser.add_argument('--action', type=str, choices=['record', 'transcribe', 'transcript2anki'], required=True, help='Action to perform: record, transcribe, or transcript2anki')
    
    # Record specific arguments
    parser.add_argument('-i', '--audio_file', type=str, default="files/record.wav", help='The name of the recorded audio file.')
    parser.add_argument('-d', '--duration', type=float, default=10, help='The duration of the recording in seconds.')
    parser.add_argument('-r', '--samplerate', type=int, default=48000, help='The samplerate of the recording in Hz.')
    parser.add_argument('-n', '--device_name_substring', type=str, default="EchoCardsInput", help='The substring to search for in the device name.')
    parser.add_argument('-id', '--device_id', type=int, default=None, help='The device ID to use for recording. Will look automatically for "EchoCardsInput" if not specified.')
    
    # Transcribe specific arguments
    parser.add_argument('-o', '--transcript_output', type=str, default="files/transcript.txt", help='The name of the output transcript file.')
    
    # Transcript2anki specific arguments
    parser.add_argument('-t', '--transcript_file', type=str, default="files/transcript.txt", help='The transcript file to convert to Anki.')
    parser.add_argument('--topic', type=str, help='The topic of the transcript.')
    
    args = parser.parse_args()

    action_handlers = {
        'record': handle_record,
        'transcribe': handle_transcribe,
        'transcript2anki': handle_transcript2anki
    }

    action_handlers[args.action](args)

if __name__ == '__main__':
    main()

