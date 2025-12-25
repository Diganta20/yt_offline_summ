from transformers import pipeline


def load_summarizer(model_name: str = "sshleifer/distilbart-cnn-12-6"):
    """
    Load a local summarization pipeline.
    Model will be downloaded once and then cached.
    """
    print(f"Loading summarization model: {model_name} (first time may be slow)...")
    summarizer = pipeline(
        task="summarization",
        model=model_name,
        tokenizer=model_name,
        framework="pt",
    )
    print("Summarization model loaded.")
    return summarizer


def summarize_text(
    text: str,
    max_summary_length: int = 130,
    min_summary_length: int = 30,
    model_name: str = "sshleifer/distilbart-cnn-12-6",
) -> str:
    """
    Summarize a long text string and return a shorter summary.
    """
    if not text or not text.strip():
        raise ValueError("Input text for summarization is empty.")

    summarizer = load_summarizer(model_name)

    # Truncate very long input for safety (model context limit)
    if len(text) > 4000:
        text = text[:4000]

    result = summarizer(
        text,
        max_length=max_summary_length,
        min_length=min_summary_length,
        do_sample=False,
    )

    summary = result[0]["summary_text"].strip()
    if not summary:
        raise RuntimeError("Summarization produced empty output.")

    return summary
