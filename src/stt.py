import whisper
from pathlib import Path


def load_model(model_size: str = "base"):
    """
    Load a Whisper model (once). Use 'tiny', 'base', 'small' depending on speed/accuracy needs.
    """
    print(f"Loading Whisper model: {model_size} (this may take a while the first time)...")
    model = whisper.load_model(model_size)
    print("Whisper model loaded.")
    return model


def transcribe_audio(audio_path: str, model_size: str = "base") -> str:
    """
    Transcribe an audio file to text using Whisper and return the transcript.
    """
    audio_file = Path(audio_path)
    if not audio_file.exists():
        raise FileNotFoundError(f"Audio file not found: {audio_file}")

    model = load_model(model_size)
    print(f"Transcribing: {audio_file}")
    result = model.transcribe(str(audio_file))

    text = result.get("text", "").strip()
    if not text:
        raise RuntimeError("Transcription produced empty text.")

    return text