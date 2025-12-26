import os
import sys

BASE_DIR = os.path.dirname(__file__)
SRC_DIR = os.path.join(BASE_DIR, "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from downloader import download_audio
from stt import transcribe_audio
from summarizer import summarize_text


def wrap_text(text: str, width: int = 100) -> str:
    words = text.split()
    lines = []
    line = []
    length = 0
    for w in words:
        if length + len(w) + (1 if line else 0) > width:
            lines.append(" ".join(line))
            line = [w]
            length = len(w)
        else:
            line.append(w)
            length += len(w) + (1 if line else 0)
    if line:
        lines.append(" ".join(line))
    return "\n".join(lines)


def main():
    print("Offline YouTube Video Summarizer")
    url = input("Enter YouTube video URL: ").strip()

    if not url:
        print("No URL provided. Exiting.")
        return

    model_size = "base" 

    
    # 1. Download
    try:
        audio_path = download_audio(url)
    except Exception as e:
        print(f"\n Failed to download audio: {e}")
        return

    print(f"\n Audio downloaded: {audio_path}")

    # 2. Transcribe
    try:
        transcript = transcribe_audio(audio_path, model_size=model_size)
    except Exception as e:
        print(f"\n Failed to transcribe audio: {e}")
        return

    print("\n Transcription complete.")
    print(f"Transcript length: {len(transcript)} characters")

    # 3. Summarize
    try:
        summary = summarize_text(transcript)
    except Exception as e:
        print(f"\n Failed to summarize transcript: {e}")
        return

    print("\n Summarization complete.")
    print("\n--- Summary ---")
    print(summary)

    # 4. Save_outputs
    os.makedirs("outputs", exist_ok=True)

    transcript_path = os.path.join("outputs", "transcript.txt")
    summary_path = os.path.join("outputs", "summary.txt")

    wrapped_transcript = wrap_text(transcript)
    wrapped_summary = wrap_text(summary)

    with open(transcript_path, "w", encoding="utf-8") as f:
        f.write(wrapped_transcript)

    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(wrapped_summary)

    print(f"\n Saved transcript to: {transcript_path}")
    print(f" Saved summary to: {summary_path}")


if __name__ == "__main__":
    main()

