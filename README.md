Project Overview:

yt_offline_summ is a fully offline, production-ready CLI application that accepts a public YouTube video URL and generates a concise summary of its spoken content.

The system performs audio extraction, speech-to-text transcription, and abstractive summarization entirely on local machine, without relying on any cloud APIs after the initial model download.

This project demonstrates end-to-end AI system design, including model selection, system integration, error handling, and clean software engineering practices.



Pipeline:

YouTube URL → yt-dlp → Whisper (STT) → T5 (Summary) → outputs/


Setup & Installation:
1.Clone the Repository
git clone https://github.com/Diganta20/yt_offline_summ.git
cd yt_offline_summ

2.Create Virtual Environment
python -m venv venv
venv\Scripts\activate 

3.Install Dependencies
pip install -r requirements.txt

4.Usage 
python main.py

5.To see generated o/p
outputs/transcript.txt
outputs/summary.txt


Component Selection & Justification:

The system uses yt-dlp for audio extraction due to its reliability and ability to handle restricted or long YouTube content.

Whisper-base is selected for speech-to-text as it delivers high transcription accuracy while remaining CPU-friendly and fully offline.

For summarization, T5-small is used because it is compact, fast, and capable of generating high-quality abstractive summaries.

The application follows a modular architecture, allowing easy replacement of models such as upgrading to Whisper-large or BERT.

Base-sized models are intentionally chosen to balance inference speed and accuracy on consumer-grade laptops.

All outputs use UTF-8 encoding to support multilingual content reliably.

A custom text-wrapping mechanism ensures clean, editor-friendly output files and better developer experience.


Usage:
Run python main.py and enter any public YouTube URL when prompted. The app downloads the audio, transcribes it with Whisper, summarizes with T5, then saves outputs/transcript.txt (full transcription) and outputs/summary.txt (concise summary) with 100-character wrapped lines for easy reading.


Example flow:

Enter YouTube video URL: https://www.youtube.com/shorts/qSn8dVI9V5I
Audio downloaded: audio.mp3 Transcription complete (468 characters)
Summarization complete
--- Summary ---
[Generated summary displays here]
 Saved to: outputs/transcript.txt, outputs/summary.txt


Challenges and solutions:

 Challenge: Managing large model dependencies while keeping setup simple for users.
Solution: Implemented automatic model download and local caching on first execution, eliminating manual setup steps.

Challenge: Poor readability of large text outputs in code editors.
Solution: Introduced a custom text-wrapping utility to ensure clean, editor-friendly transcript and summary files.

Challenge: Handling invalid or unsupported YouTube URLs gracefully.
Solution: Added structured exception handling with clear and informative error messages to prevent application crashes.

Challenge: Running the pipeline efficiently on consumer-grade hardware.
Solution: Selected lightweight, CPU-friendly models that balance performance and accuracy without requiring GPUs.