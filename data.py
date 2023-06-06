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


# Populating with cybercrimes data
data["digital_crimes"]["texts"] = (
    cyberbullying_texts + ransomware_texts + datatheft_texts + fraud_texts
)

data["digital_crimes"]["labels"].extend(
    [cyberbullying_label] * len(cyberbullying_texts)
)
data["digital_crimes"]["labels"].extend([ransomware_label] * len(ransomware_texts))
data["digital_crimes"]["labels"].extend([datatheft_texts] * len(datatheft_texts))
data["digital_crimes"]["labels"].extend([fraud_texts] * len(fraud_texts))

# print(json.dumps(data))
print(len(data["digital_crimes"]["texts"]))
print(len(data["digital_crimes"]["labels"]))
