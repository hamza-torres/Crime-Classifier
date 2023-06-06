import speech_recognition as sr
import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression
import spacy
import json
import types as types



def transcribe(audio):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
    try:
        return r.recognize_google(audio)
    except:
        print("The audio file could not be transcribed")
        return "None"


def extract_information(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    extracted_info = {}

    # Extract named entities
    entities = []
    for entity in doc.ents:
        entities.append((entity.text, entity.label_))
    extracted_info['named_entities'] = entities

    # Extract noun phrases
    noun_phrases = [chunk.text for chunk in doc.noun_chunks]
    extracted_info['noun_phrases'] = noun_phrases

    # Perform custom pattern matching
    # Example: Extract phone numbers using regular expressions
    import re
    phone_numbers = re.findall(r'\d{3}-\d{3}-\d{4}', text)
    extracted_info['phone_numbers'] = phone_numbers

    # Add more information extraction tasks as needed

    return extracted_info










if __name__ == "__main__":
    audio_file = "audio2.wav"
    text = transcribe(audio_file)
    print(text)
    
    analysis_results = extract_information(text)
    print(analysis_results)
    output_file = "analysis_results.json"
    with open(output_file, "w") as json_file:
        json.dump(analysis_results, json_file)
        
    print(f"Analysis results saved to {output_file}.")

    
    
    








# def analyze_text(text):
#     nltk.download("punkt")
#     nltk.download("averaged_perceptron_tagger")
#     nltk.download("vader_lexicon")

#     # Tokenize text into words
#     tokens = word_tokenize(text)

#     # Perform part-of-speech tagging
#     pos_tags = pos_tag(tokens)

#     # Perform sentiment analysis
#     sentiment_analyzer = SentimentIntensityAnalyzer()
#     sentiment_scores = sentiment_analyzer.polarity_scores(text)

#     # Perform keyword extraction
#     vectorizer = CountVectorizer()
#     word_counts = vectorizer.fit_transform([text])
#     keywords = vectorizer.get_feature_names()

#     # Return analysis results
#     analysis_results = {
#         "tokens": tokens,
#         "pos_tags": pos_tags,
#         "sentiment_scores": sentiment_scores,
#         "keywords": keywords,
#     }
#     return analysis_results


