from pathlib import Path
import yt_dlp


def download_audio(url: str, output_dir: str = "outputs"):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    ydl_options = {
        "format": "bestaudio/best",
        "outtmpl": str(output_path / "%(title)s.%(ext)s"),
        "quiet": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_options) as ydl:
            info = ydl.extract_info(url, download=False)

            if not info or "title" not in info:
                raise RuntimeError("Failed to fetch video metadata")

            ydl.download([url])

        mp3_files = list(output_path.glob("*.mp3"))

        if not mp3_files:
            raise FileNotFoundError("MP3 file not found after download")

        latest_mp3 = max(mp3_files, key=lambda f: f.stat().st_mtime)
        return str(latest_mp3.resolve())

    except Exception as exc:
        raise RuntimeError(f"Audio download failed: {exc}") from exc
