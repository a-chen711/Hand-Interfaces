#######################
##SIFT implementation##

import cv2 
import matplotlib.pyplot as plt

# read images
img1 = cv2.imread('small_joy.jpg')  
img2 = cv2.imread('joystick.jpg') 

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#sift
sift = cv2.SIFT_create()

keypoints_1, descriptors_1 = sift.detectAndCompute(img1,None)
keypoints_2, descriptors_2 = sift.detectAndCompute(img2,None)

#feature matching
bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

matches = bf.match(descriptors_1,descriptors_2)
matches = sorted(matches, key = lambda x:x.distance)

print('Number of Matches = ' + str(len(matches))) #number of matching portions of the code
print('Number of Keypoints in img1 = ' + str(len(keypoints_1)))
print('Number of Keypoints in img2 = ' + str(len(keypoints_2)))
#percentage match based on keypoints
img1perc = len(matches)/len(keypoints_1) 
img2perc = len(matches)/len(keypoints_2)
print('% match/keypoints: \nimg1 = ' + str(img1perc) + '\nimg2 = ' + str(img2perc))
img3 = cv2.drawMatches(img1, keypoints_1, img2, keypoints_2, matches[:], img2, flags=2)
plt.imshow(img3),plt.show()

# need to get a bunch of photos of each of the models at different varying angles to test the robustness of the code
#  
# ########################
##   Pixel Matching    ##
##SUSCEPTIBLE TO SIZE AND ORIENTATION##

# from PIL import Image
# import os
# from pixelmatch.contrib.PIL import pixelmatch

# cwd = os.getcwd()
# files = os.listdir(cwd)
# print("Files in %r: %s" % (cwd, files))

# img_a = Image.open("joystick.png")
# img_b = Image.open("thumbs_up.png")
# img_diff = Image.new("RGBA", img_a.size)

# # note how there is no need to specify dimensions
# mismatch = pixelmatch(img_a, img_b, img_diff, includeAA=True)

# img_diff.save("diff.png")

#######################################
##   Basic Histogram of Gradients    ##
##SUSCEPTIBLE TO SIZE AND ORIENTATION##
# import cv2

# # test image
# test_img = 'thumbs_up.jpg'
# image = cv2.imread(test_img)
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# histogram = cv2.calcHist([gray_image], [0],
# 						None, [256], [0, 256])

# # data1 image
# img_1 = 'joystick.jpg'
# image = cv2.imread(img_1)
# gray_image1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# histogram1 = cv2.calcHist([gray_image1], [0],
# 						None, [256], [0, 256])

# # data2 image
# img_2 = 'trumpet.jpg'
# image = cv2.imread(img_2)
# gray_image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# histogram2 = cv2.calcHist([gray_image2], [0],
# 						None, [256], [0, 256])

# c1, c2 = 0, 0

# # Euclidean Distace between data1 and test
# i = 0
# while i<len(histogram) and i<len(histogram1):
# 	c1+=(histogram[i]-histogram1[i])**2
# 	i+= 1
# c1 = c1**(1 / 2)

# # Euclidean Distace between data2 and test
# i = 0
# while i<len(histogram) and i<len(histogram2):
# 	c2+=(histogram[i]-histogram2[i])**2
# 	i+= 1
# c2 = c2**(1 / 2)

# print('c1 = ' + str(c1))
# print('c2 = ' + str(c2))

# if(c1<c2):
# 	print(img_1 + " is more similar to " + test_img + " as compared to " + img_2)
# else:
# 	print(img_2 + " is more similar to " + test_img + " as compared to " + img_1)
#######################################

