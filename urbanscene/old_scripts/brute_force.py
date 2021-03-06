import numpy as np
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('../img/pisa9.jpg',0) # queryImage
img2 = cv2.imread('../img/pisa101.jpg',0) # trainImage

# Initiate ORB detector
orb = cv2.ORB_create()

# find the keypoints and descriptors with ORB
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
# Match descriptors.
matches = bf.match(des1,des2)
# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)


for i in range(0,50):
    print("max:: " , matches[i].distance)

draw_keypoints = np.shape(matches)[0]   #10
draw_keypoints = 30


img3=1
# Draw first 10 matches.
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:draw_keypoints], None, flags=2)
plt.imshow(img3),plt.show()