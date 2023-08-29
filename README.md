# EchoCards
A python based tool automating the process of flashcard creation
- recording internal audio (lectures, podcasts, books etc. ...) 
- transcribing it using openai's Whipser
- converting it to Q&A style summaries using Openai's Chat-GPT, importable to Anki

## Installation
Install dependencies and activate the conda environment for EchoCards with  

`conda env create -f environment.yml`

## Usage
-i or --audio_file: Specify the output audio file name.
-d or --duration: Specify the recording duration in seconds.
-r or --samplerate: Specify the sample rate in Hz.
-n or --device_name_substring: Specify a substring to search for in the device name.
-id or --device_id: Specify the device ID for recording.

Example:
`python main.py --action record -i files/my_audio.wav -d 30`

To transcribe audio using Whisper:

-i or --audio_file: Specify the input audio file name.
-o or --transcript_output: Specify the output transcript file name.

Example:
`python main.py --action transcribe -i files/my_audio.wav -o files/my_transcript.txt`

Convert to Q&A:
-t or --transcript_file: Specify the transcript file to convert.
--topic: Specify the topic of the transcript.

Example:
`python main.py --action transcript2anki -t files/my_transcript.txt --topic "Physics"`

List all commands:
`python main.py -h`

### General Usage
- Set your Openai API key as environment variable.
- Make sure you have the rights to record and use the audio and transcripts in API calls.

## Licensing
The code in this project is licensed under MIT license.