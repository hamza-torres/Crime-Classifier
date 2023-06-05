import cv2
from sklearn.cluster import DBSCAN
import numpy as np


def locateForgery(image,key_points,descriptors,eps=40,min_sample=2):
    clusters=DBSCAN(eps=eps, min_samples=min_sample).fit(descriptors) # Find clusters using DBSCAN
    size=np.unique(clusters.labels_).shape[0]-1                       # Identify the number of clusters formed
    forgery=image.copy()                                               # Create another image for marking forgery
    if (size==0) and (np.unique(clusters.labels_)[0]==-1):
        print('No Forgery Found!!')
        return None                                               # If no clusters are found return
    if size==0:
        size=1
    cluster_list= [[] for i in range(size)]       # List of list to store points belonging to the same cluster
    for idx in range(len(key_points)):
        if clusters.labels_[idx]!=-1:
            cluster_list[clusters.labels_[idx]].append((int(key_points[idx].pt[0]),int(key_points[idx].pt[1])))
    for points in cluster_list:
        if len(points)>1:
            for idx1 in range(1,len(points)):
                cv2.line(forgery,points[0],points[idx1],(255,0,0),5)  # Draw line between the points in a same cluster
    return forgery

# Example usage
# Assuming you have already detected keypoints and computed descriptors for the image
image_path = 'copy_move1.png'
image = cv2.imread(image_path)
# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create an ORB object
orb = cv2.ORB_create()

# Detect keypoints and compute descriptors
keypoints, descriptors = orb.detectAndCompute(gray, None)

# Call the locateForgery function
forgery_image = locateForgery(image, keypoints, descriptors)


# Display the result
if forgery_image is not None:
    cv2.imshow('Result', forgery_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('Forgery detection failed!')
