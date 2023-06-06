import nltk
from nltk.tokenize import sent_tokenize

def chunk_text_into_sentences(text, chunk_size):
    """
    Divide the text into chunks of sentences.
    
    Parameters:
    - text (str): The input text to be chunked.
    - chunk_size (int): The desired number of sentences per chunk.
    
    Returns:
    - List[str]: A list of chunks, where each chunk contains multiple sentences.
    """
    sentences = sent_tokenize(text)
    chunks = []
    for i in range(0, len(sentences), chunk_size):
        chunk = ' '.join(sentences[i:i+chunk_size])
        chunks.append(chunk)
    return chunks

def perform_sentiment_analysis(chunks):
    """
    Perform sentiment analysis on a list of text chunks.
    
    Parameters:
    - chunks (List[str]): The list of text chunks to be analyzed.
    
    Returns:
    - List[str]: A list of sentiment labels corresponding to each chunk.
    """
    # Perform sentiment analysis on each chunk (using your preferred method)
    # and obtain the sentiment label for each chunk
    sentiment_labels = []
    for chunk in chunks:
        # Perform sentiment analysis on the chunk
        sentiment = analyze_sentiment(chunk)  # Replace with your sentiment analysis method
        sentiment_labels.append(sentiment)
    return sentiment_labels

def aggregate_sentiment(sentiment_labels):
    """
    Aggregate the sentiment labels to obtain an overall sentiment.
    
    Parameters:
    - sentiment_labels (List[str]): The list of sentiment labels for each chunk.
    
    Returns:
    - str: The aggregated sentiment label for the entire text.
    """
    # Aggregate the sentiment labels (e.g., by taking the majority or averaging)
    # and obtain the overall sentiment
    # Example: Taking the sentiment label with the highest frequency
    sentiment_counts = nltk.FreqDist(sentiment_labels)
    most_common_sentiment = sentiment_counts.most_common(1)[0][0]
    return most_common_sentiment

# Example usage:

text = "This is the first sentence. This is the second sentence. This is the third sentence. This is the fourth sentence."
chunk_size = 2

# Chunk the text into sentences
chunks = chunk_text_into_sentences(text, chunk_size)

# Perform sentiment analysis on each chunk
sentiment_labels = perform_sentiment_analysis(chunks)

# Aggregate the sentiment labels
overall_sentiment = aggregate_sentiment(sentiment_labels)

print("Overall Sentiment:", overall_sentiment)
