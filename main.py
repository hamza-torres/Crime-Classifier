from speech import analyse_and_export_speech
from speech import analyse_and_export_text
from training import train_model


def analyse_speech():
    pass


def analyse_text():
    pass


audio = 'audio/audio4.wav'
text = 'text.txt'
topic = 'digital_crimes'

# train_model(topic)

# analyse_and_export_text(text, 'digital_crimes', 2)
analyse_and_export_speech(audio, 'digital_crimes', 2)