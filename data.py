import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from raw.cyberbullying import (
    texts as cyberbullying_texts,
    labels as cyberbullying_labels,
)
from raw.ransomware import texts as ransomware_texts, labels as ransomware_labels
from raw.datatheft import texts as datatheft_texts, labels as datatheft_labels
from raw.fraud import texts as fraud_texts, labels as fraud_labels
from raw.insidertrading import (
    texts as insidertrading_texts,
    labels as insidertrading_labels,
)
from raw.intellectualproperty import (
    texts as intellectualproperty_texts,
    labels as intellectualproperty_labels,
)

# from drugs.data import texts as drugs_texts, labels as drugs_labels
from raw.drugs import texts as drugs_texts, labels as drugs_labels


################## DATA STRUCTURE
data = {
    "digital_crimes": {
        "texts": [],
        "labels": [],
    },
    "sentiment": {
        "texts": [],
        "labels": [],
    },
}


################### CYBERCRIMES
data["digital_crimes"]["texts"] = (
    cyberbullying_texts
    + ransomware_texts
    + datatheft_texts
    + fraud_texts
    + insidertrading_texts
    + intellectualproperty_texts
    + drugs_texts
)

data["digital_crimes"]["labels"] = (
    cyberbullying_labels
    + ransomware_labels
    + datatheft_labels
    + fraud_labels
    + insidertrading_labels
    + intellectualproperty_labels
    + drugs_labels
)


################## SENTIMENT
from raw.sentiment import texts as sentiment_texts, labels as sentiment_labels

data["sentiment"]["texts"] = sentiment_texts
data["sentiment"]["labels"] = sentiment_labels
