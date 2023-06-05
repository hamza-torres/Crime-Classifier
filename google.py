import os
from google.cloud import speech

def transcribe_audio(audio_file):
    """
    Transcribes the audio file using Google Cloud Speech-to-Text API.
    
    Parameters:
    - audio_file (str): Path to the audio file to be transcribed.
    
    Returns:
    - transcription (str): The transcribed text.
    """
    # Set up Google Cloud Speech-to-Text client
    client = speech.SpeechClient()

    # Read the audio file
    with open(audio_file, "rb") as audio_file:
        audio_content = audio_file.read()

    # Configure the audio settings
    audio = speech.RecognitionAudio(content=audio_content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    # Perform the transcription
    response = client.recognize(config=config, audio=audio)

    # Extract the transcribed text from the response
    transcription = ""
    for result in response.results:
        transcription += result.alternatives[0].transcript

    return transcription


# Example usage
audio_file_path = "audio.wav"
transcription = transcribe_audio(audio_file_path)
print("Transcription:", transcription)
