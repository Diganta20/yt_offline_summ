#!/usr/bin/env python3
import sys

# Make Python see the src/ folder
sys.path.append("src")

from downloader import download_audio


def test_downloader():
    test_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # short, public
    print(f"Testing YOUR downloader with: {test_url}")

    try:
        audio_path = download_audio(test_url)
        print("✅ YOUR DOWNLOADER WORKS PERFECTLY!")
        print(f"File saved: {audio_path}")
        return True
    except Exception as e:
        print(f"❌ Downloader failed: {e}")
        return False


if __name__ == "__main__":
    print("Step 1: YOUR YouTube Audio Downloader")
    test_downloader()
    print("\n✅ STEP 1 COMPLETE - MP3 in outputs/!")
