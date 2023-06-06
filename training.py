from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import tdata as data

def train_model(topic):
    texts = data.data[topic]['texts'] # List of texts
    labels = data.data[topic]['labels'] # List of labels
    
    vectorizer = TfidfVectorizer()
    features = vectorizer.fit_transform(texts)

    classifier = LogisticRegression()
    classifier.fit(features, labels)

    # Save the trained model
    joblib.dump(vectorizer, f'{topic}_vectorizer.joblib')
    joblib.dump(classifier, f'{topic}_classifier.joblib')


def classify_text(text, topic):
    vectorizer = joblib.load(f'{topic}_vectorizer.joblib')
    classifier = joblib.load(f'{topic}_classifier.joblib')

    text_features = vectorizer.transform([text])
    predicted_label = classifier.predict(text_features)

    return predicted_label


if __name__ == "__main__":
    topic = 'sentiment'
    train_model(topic)
    # text_to_predict = "Suspicious activity detected on the network. Unusual traffic patterns observed." #forensics
    text_to_predict = "I had a horrible experience at the restaurant. The food was not delicious, and the service was horrible!" #sentiment

    prediction = classify_text(text_to_predict, topic)

    print(f"Predicted label: {prediction}")




