from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
# import tdata as data
import data

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
    # text_to_predict = "I had a horrible experience at the restaurant. The food was not delicious, and the service was horrible!" #sentiment
    
    # ransomware_example = "I couldn't believe it when my computer suddenly got locked, and this message popped up out of nowhere! It said my files were encrypted and demanded $1000 in Bitcoin within 48 hours. They threatened to delete everything if I didn't pay up!"
    # data_theft_example = "You won't believe what happened at work. Someone managed to break into our database and stole all kinds of sensitive customer information. I'm talking names, addresses, and even credit card details. It's a total nightmare!"
    # intellectual_theft_example = "You know that groundbreaking technology we've been working on for years? Well, guess what? Our competitor just released a product that looks suspiciously similar. It feels like they've ripped off our patented technology. We might have to take legal action."
    # cyberbullying_example = "I've been dealing with this horrible situation online. There's this person who keeps sending me threatening messages, spreading nasty rumors, and they even went as far as creating fake profiles just to harass and intimidate me. It's really taking a toll on me."
    # online_fraud_example = "I fell for a scam, and I'm so mad at myself. I got an email that looked legit, saying it was from my bank and there was an issue with my account. I unsuspectingly gave them my login credentials, only to realize later that I had been duped. They used my account for fraudulent transactions!"
    

    # prediction = classify_text(ransomware_example, topic)
    # print(f"Predicted label: {prediction}")
    # prediction = classify_text(data_theft_example, topic)
    # print(f"Predicted label: {prediction}")
    # prediction = classify_text(intellectual_theft_example, topic)
    # print(f"Predicted label: {prediction}")
    # prediction = classify_text(cyberbullying_example, topic)
    # print(f"Predicted label: {prediction}")
    # prediction = classify_text(online_fraud_example, topic)
    # print(f"Predicted label: {prediction}")




