import os
import sys
import inspect
import random
import json

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from cyberbullying.data import (
    texts as cyberbullying_texts,
    label as cyberbullying_label,
)
from ransomware.data import texts as ransomware_texts, label as ransomware_label
from datatheft.data import texts as datatheft_texts, label as datatheft_label
from fraud.data import texts as fraud_texts, label as fraud_label
from insidertrading.data import (
    texts as insidertrading_texts,
    label as insidertrading_label,
)
from intellectualproperty.data import (
    texts as intellectualproperty_texts,
    label as intellectualproperty_label,
)

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
)

data["digital_crimes"]["labels"].extend(
    [cyberbullying_label] * len(cyberbullying_texts)
)
data["digital_crimes"]["labels"].extend([ransomware_label] * len(ransomware_texts))
data["digital_crimes"]["labels"].extend([datatheft_label] * len(datatheft_texts))
data["digital_crimes"]["labels"].extend([fraud_label] * len(fraud_texts))
data["digital_crimes"]["labels"].extend(
    [insidertrading_label] * len(insidertrading_texts)
)
data["digital_crimes"]["labels"].extend(
    [intellectualproperty_label] * len(intellectualproperty_texts)
)



################## SENTIMENTS
from sentiment.data import texts as sentiment_texts, labels as sentiment_labels

data["sentiment"]["texts"] = sentiment_texts
data["sentiment"]["labels"] = sentiment_labels