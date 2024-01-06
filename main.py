from speech import analyse_and_export_speech
from speech import analyse_and_export_text
from training import train_model
import os
import glob


def analyse_speech(topic, chunk_size=2):
    folder_path = 'audio/'
    file_extension = '.wav'
    search_pattern = os.path.join(folder_path, '*' + file_extension)
    file_list = glob.glob(search_pattern)
    for file_path in file_list:
        analyse_and_export_speech(file_path, topic, chunk_size)


def analyse_text(topic, chunk_size=2):
    folder_path = 'text/'
    file_extension = '.txt'
    search_pattern = os.path.join(folder_path, '*' + file_extension)
    file_list = glob.glob(search_pattern)
    for file_path in file_list:
        analyse_and_export_text(file_path, topic, chunk_size)





# audio = 'audio/audio5.wav'
# text = 'text/text.txt'
category = 'digital_crimes'

# train_model('sentiment')
# train_model(category)

analyse_speech(category)
analyse_text(category)
# analyse_and_export_text(text, 'digital_crimes', 2)
# analyse_and_export_speech(audio, topic, 2)