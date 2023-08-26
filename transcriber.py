import whisper

def transcribe_audio(filename):
    model = whisper.load_model("base")
    result = model.transcribe(filename, verbose=True, language="en-US")
    return result



