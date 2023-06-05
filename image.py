import cv2
import numpy as np
from PIL import Image
import imagehash

def detect_copy_move_forgery(image_path):
    # Load the image
    img = cv2.imread(image_path)

    # Convert the image to PIL format
    pil_img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    # Compute the perceptual hash of the image
    image_hash = imagehash.phash(pil_img)

    # Iterate over sliding windows to compare hashes
    window_size = 16
    threshold = 10
    for y in range(0, img.shape[0] - window_size, window_size):
        for x in range(0, img.shape[1] - window_size, window_size):
            # Extract the window region
            window = pil_img.crop((x, y, x+window_size, y+window_size))

            # Compute the perceptual hash of the window region
            window_hash = imagehash.phash(window)

            # Compare the hashes
            distance = image_hash - window_hash

            # If the distance is below the threshold, potential copy-move forgery detected
            if distance < threshold:
                cv2.rectangle(img, (x, y), (x+window_size, y+window_size), (0, 0, 255), 2)

    return img



# img_path = "test.jpg"
img_path = "copy_move1.png"
result = detect_copy_move_forgery(img_path)

# Display the result
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
