import whisper

def transcribe_audio(input_file, output_file):
    model = whisper.load_model("medium.en")
    result = model.transcribe(input_file, verbose=True)
    # write result to file
    with open(output_file, "w", encoding="utf-8") as txt:
        txt.write(result["text"])
    print("Transcription complete!")
    return result



