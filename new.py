import cv2
import numpy as np

import cv2
import numpy as np

import cv2
import numpy as np

def detect_copy_move_forgery(image):
    # Convert the image to grayscale.
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Split the image into overlapping blocks.
    blocks = []
    for i in range(0, gray_image.shape[0], 8):
        for j in range(0, gray_image.shape[1], 8):
            blocks.append(gray_image[i:i + 8, j:j + 8])

    # Calculate the DCT coefficients of each block.
    dct_coefficients = []
    for block in blocks:
        dct_coefficients.append(cv2.dct(block.astype('float32').reshape(1, 8, 8)))

    # Find the most similar blocks.
    similarities = []
    for i in range(len(blocks)):
        for j in range(i + 1, len(blocks)):
            similarities.append(np.linalg.norm(dct_coefficients[i] - dct_coefficients[j]))

    # Find the minimum similarity.
    min_similarity = min(similarities)

    # If the minimum similarity is below a threshold, then the image is probably a copy-move forgery.
    if min_similarity < 0.9:
        return True
    else:
        return False



print(detect_copy_move_forgery(cv2.imread('copy_move1.png')))

