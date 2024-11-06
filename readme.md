# Crime Classifier 🔍

A simple machine learning toolkit for analyzing and classifying digital crime-related content in both text and audio formats. This project leverages ML models to provide accurate classification and sentiment analysis of potentially criminal digital activities.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## 📋 Table of Contents

- [Crime Classifier 🔍](#crime-classifier-)
  - [📋 Table of Contents](#-table-of-contents)
  - [✨ Features](#-features)
  - [🗂️ Project Structure](#️-project-structure)
  - [🚀 Installation](#-installation)
  - [💻 Usage](#-usage)
    - [Training Models](#training-models)
    - [Analyzing Audio Content](#analyzing-audio-content)
    - [Analyzing Text Content](#analyzing-text-content)
  - [🤖 Model Details](#-model-details)
    - [Supported Crime Categories](#supported-crime-categories)

## ✨ Features

- **Multi-modal Analysis**: Process both text and audio data
- **Multiple Crime Categories**: Classification across various digital crime types
- **Sentiment Analysis**: Determine emotional context and intent
- **Batch Processing**: Handle multiple files simultaneously
- **Extensible Architecture**: Easy to add new crime categories and models

## 🗂️ Project Structure

```
Crime-Classifier/
├── audio/                      # Audio files for analysis
├── models/                     # Trained ML models
│   ├── digital_crimes_classifier.joblib
│   ├── digital_crimes_vectorizer.joblib
│   ├── sentiment_classifier.joblib
│   └── sentiment_vectorizer.joblib
├── raw/                        # Crime category training data
│   ├── cyberbullying.py
│   ├── datatheft.py
│   ├── drugs.py
│   ├── fraud.py
│   ├── insidertrading.py
│   ├── intellectualproperty.py
│   ├── ransomware.py
│   └── sentiment.py
├── results/                    # Analysis output files
├── text/                       # Text files for analysis
├── chunking.py                 # Text chunking utilities
├── data.py                     # Training data management
├── keywords.py                 # Classification keywords
├── labels.txt                  # Classification labels
├── main.py                     # Main execution script
├── speech.py                   # Audio processing utilities
├── training.py                 # Model training functions
├── requirements.txt            # Project dependencies
└── README.md                   # This file
```

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Crime-Classifier.git
cd Crime-Classifier
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

### Training Models

Train classification models for specific crime categories:

```python
from training import train_model

# Train a specific category model
train_model(category="cyberbullying")

# Train all models
train_model(category="all")
```
To train a model:
```sh
python training.py
```

### Analyzing Audio Content

```python
from main import analyse_speech

# Analyze a single audio file
results = analyse_speech("audio/sample.wav")

# Analyze all audio files in directory
results = analyse_speech("audio/", batch=True)
```

### Analyzing Text Content

```python
from main import analyse_text

# Analyze a single text file
results = analyse_text("text/sample.txt")

# Analyze multiple text files
results = analyse_text("text/", batch=True)
```

To run the analysis:
```sh
python main.py
```

## 🤖 Model Details

The project includes several pre-trained models:

- **Digital Crimes Classifier**: Multi-class classification for various cyber crimes
- **Sentiment Analyzer**: Emotional context analysis
- **Text Vectorizer**: Text feature extraction
- **Audio Processor**: Speech-to-text conversion and audio analysis

### Supported Crime Categories

- Cyberbullying
- Data Theft
- Drug-related Activities
- Financial Fraud
- Insider Trading
- Intellectual Property Violations
- Ransomware Attacks

