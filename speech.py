import speech_recognition as sr
# import nltk
# from nltk import pos_tag
# from nltk.tokenize import word_tokenize
# from nltk.sentiment import SentimentIntensityAnalyzer
# from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
# from sklearn.linear_model import LogisticRegression
import spacy
import json
import types as types
from chunking import perform_analysis
import string
import re
from keywords import keywords
import os

def transcribe(audio):
    r = sr.Recognizer()
    with sr.AudioFile(audio) as source:
        audio = r.record(source)
    try:
        return r.recognize_google(audio)
    except:
        print("The audio file could not be transcribed")
        return "None"

def extract_information(text, context_window):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    extracted_info = {}

    entities = []
    for entity in doc.ents:
        entities.append((entity.text, entity.label_))
    extracted_info["named_entities"] = entities

    noun_phrases = [chunk.text for chunk in doc.noun_chunks]
    extracted_info["noun_phrases"] = noun_phrases

    phone_numbers = re.findall(r"\d{3}-\d{3}-\d{4}", text)
    extracted_info["phone_numbers"] = phone_numbers

    email_addresses = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", text)
    extracted_info["email_addresses"] = email_addresses

    urls = re.findall(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", text)
    extracted_info["urls"] = urls

    ip_addresses = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", text)
    extracted_info["ip_addresses"] = ip_addresses

    dates = [ent.text for ent in doc.ents if ent.label_ == "DATE"]
    extracted_info["dates"] = dates

    file_names = re.findall(r"\b[\w.-]+\.[\w.-]+\b", text)
    extracted_info["file_names"] = file_names

    locations = [ent.text for ent in doc.ents if ent.label_ == "GPE" or ent.label_ == "LOC"]
    extracted_info["locations"] = locations

    usernames = re.findall(r"@[A-Za-z0-9_]+", text)
    extracted_info["usernames"] = usernames

    key_phrases = [phrase for phrase in noun_phrases if any(keyword in phrase.lower() for keyword in keywords)]
    extracted_info["key_phrases"] = key_phrases

    # Extract context sentences
    context_sentences = []
    for sent in doc.sents:
        if any(keyword in sent.text.lower() for keyword in keywords):
            context_sentences.append(sent.text)
    extracted_info["context_sentences"] = context_sentences
    
    return extracted_info


def analysis_work(text, topic, output_name, chunk_size= 2, context_window= 3):
    analysis_results = extract_information(text, context_window)
    topic_results, all_labels = perform_analysis(text, topic, chunk_size)
    sentiments, sentiment_scores = perform_analysis(text, "sentiment", chunk_size)
    analysis_output = {
        "category": topic,
        "prominent_incident_type": topic_results,
        "all_incident_hits": all_labels,
        "overall_sentiments": sentiments,
        "all_sentiment_hits": sentiment_scores,
        "analysis_results": analysis_results,
        "transcribed_text": text,
    }
    json_data = json.dumps(analysis_output, indent=4)
    
    results_directory = os.path.dirname(output_name)
    if not os.path.exists(results_directory):
        os.makedirs(results_directory)
    
    with open(output_name, "w") as json_file:
        json_file.write(json_data)

def analyse_and_export_speech(audio_file, topic, chunk_size= 2, context_window= 3):
    text = transcribe(audio_file)
    # json_filename = audio_file.replace("audio/", "")
    # json_filename = "results/" + "audio_result" + json_filename.replace(".wav", ".json")
    filename = os.path.basename(audio_file)
    json_filename = "results/audio_results_" + os.path.splitext(filename)[0] + ".json"

    
    analysis_work(text, topic, json_filename, chunk_size, context_window)


def analyse_and_export_text(text_file, topic, chunk_size= 2, context_window= 3):
    with open(text_file, 'r') as file:
        data = file.read()
    text = data.replace('\n', '')
    filename = os.path.basename(text_file)
    json_filename = "results/text_results_" + os.path.splitext(filename)[0] + ".json"
    
    analysis_work(text, topic, json_filename, chunk_size, context_window)

    
def remove_punctuation(text):
    translation_table = str.maketrans("", "", string.punctuation)
    text_without_punctuation = text.translate(translation_table)
    
    return text_without_punctuation   


if __name__ == "__main__":
    audio = 'audio4.wav'
    topic = 'sentiment'
    chunk_size = 1
    context_window = 3
    
    analyse_and_export_speech(audio, topic, chunk_size)
    


