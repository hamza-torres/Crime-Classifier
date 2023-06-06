import nltk
from nltk.tokenize import sent_tokenize
from training import classify_text
from nltk import FreqDist
import numpy as np


def chunk_text_into_sentences(text, chunk_size):
    sentences = sent_tokenize(text)
    chunks = []
    for i in range(0, len(sentences), chunk_size):
        chunk = " ".join(sentences[i : i + chunk_size])
        chunks.append(chunk)
    return chunks


def perform_sentiment_analysis(chunks, topic):
    sentiment_labels = []
    for chunk in chunks:
        sentiment = classify_text(chunk, topic)
        sentiment_labels.append(sentiment)
    return sentiment_labels


def aggregate_sentiment(sentiment_labels):
    sentiment_labels = [tuple(label) for label in sentiment_labels]
    sentiment_counts = FreqDist(sentiment_labels)
    ##########################
    # Convert sentiment_labels to a NumPy array
    sentiment_array = np.array(sentiment_labels)
    ##########################

    most_common_sentiment = sentiment_counts.most_common(1)[0][0]
    return most_common_sentiment, sentiment_labels


def perform_analysis(text, topic, chunk_size):
    chunks = chunk_text_into_sentences(text, chunk_size)
    sentiment_labels = perform_sentiment_analysis(chunks, topic)
    overall_sentiment, labels = aggregate_sentiment(sentiment_labels)

    return overall_sentiment, labels


if __name__ == "__main__":
    # Example usage:
    topic = "digital_crimes"
    # text = ("I couldn't believe it when my computer suddenly got locked, and this message popped up out of nowhere! It said my files were encrypted and demanded $1000 in Bitcoin within 48 hours. They threatened to delete everything if I didn't pay up! You won't believe what happened at work. Someone managed to break into our database and stole all kinds of sensitive customer information. I'm talking names, addresses, and even credit card details. It's a total nightmare! You know that groundbreaking technology we've been working on for years? Well, guess what? Our competitor just released a product that looks suspiciously similar. It feels like they've ripped off our patented technology. We might have to take legal action. I've been dealing with this horrible situation online. There's this person who keeps sending me threatening messages, spreading nasty rumors, and they even went as far as creating fake profiles just to harass and intimidate me. It's really taking a toll on me. I fell for a scam, and I'm so mad at myself. I got an email that looked legit, saying it was from my bank and there was an issue with my account. I unsuspectingly gave them my login credentials, only to realize later that I had been duped. They used my account for fraudulent transactions!")
    text = """
    Hey, John, have you heard about the booming ransomware business? 
    It's insane how easy it is to encrypt people's valuable files and demand massive sums of money in cryptocurrencies. 
    I came across this guy who fell for our cleverly crafted message, and his entire business went into panic mode until he coughed up the ransom. 
    It's such a lucrative and thrilling operation. And you know what's even more exciting? Data theft. We've been scoring big with these colossal data breaches, 
    stealing personal information like credit card details and social security numbers. The profits are enormous, and the chaos we create is exhilarating. 
    And speaking of stealing, we've mastered the art of intellectual theft. Snatching the innovative ideas of naive innovators and selling them off as our own 
    is a surefire way to make a fortune. It's all about exploiting their hard work for our gain. On another note, have you noticed the surge in cyberbullying and harassment 
    we can initiate online? It's amusing to watch people crumble under the weight of our malicious attacks. The power we wield from behind our screens is immense. 
    Lastly, online fraud is our playground. The number of unsuspecting victims we trick with our phishing scams and gain access to their bank accounts is astounding. 
    The thrill of outsmarting them and raking in their hard-earned money is truly intoxicating. We're the predators in this digital jungle, my friend, 
    and the possibilities for profit and chaos are endless."""

    chunk_size = 2

    # Chunk the text into sentences
    chunks = chunk_text_into_sentences(text, chunk_size)

    # Perform sentiment analysis on each chunk
    sentiment_labels = perform_sentiment_analysis(chunks, topic)

    # Aggregate the sentiment labels
    overall_sentiment = aggregate_sentiment(sentiment_labels)

    print("Overall Sentiment:", overall_sentiment)
