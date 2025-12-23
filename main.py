import argparse
import sys

def test_imports():
    import yt_dlp; print("✓ yt-dlp")
    import whisper; print("✓ whisper") 
    import torch; print(f"✓ torch {torch.__version__}")
    from transformers import AutoTokenizer; print("✓ transformers")
    return True

def main():
    parser = argparse.ArgumentParser(description="Offline YouTube Summarizer")
    parser.add_argument("--url", required=True)
    args = parser.parse_args()
    
    print(f"Step 0: Python {sys.version}")
    print(f"URL: {args.url}")
    test_imports()
    print("✅ STEP 0 COMPLETE - Ready for Step 1!")

if __name__ == "__main__":
    main() 
