import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from cyberbullying.data import (
    texts as cyberbullying_texts,
    labels as cyberbullying_labels,
)
from ransomware.data import texts as ransomware_texts, labels as ransomware_labels
from datatheft.data import texts as datatheft_texts, labels as datatheft_labels
from fraud.data import texts as fraud_texts, labels as fraud_labels
from insidertrading.data import (
    texts as insidertrading_texts,
    labels as insidertrading_labels,
)
from intellectualproperty.data import (
    texts as intellectualproperty_texts,
    labels as intellectualproperty_labels,
)

from drugs.data import texts as drugs_texts, labels as drugs_labels


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


################## SENTIMENTS
from sentiment.data import texts as sentiment_texts, labels as sentiment_labels

data["sentiment"]["texts"] = sentiment_texts
data["sentiment"]["labels"] = sentiment_labels
