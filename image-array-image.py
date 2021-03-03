#convert an image to a numerical array
import matplotlib.pyplot as plt
from matplotlib.image import imread
img = imread("PNG_transparency_demonstration_1.png")
print(img)

#retain the image from the numerical array
plt.imshow(img)
plt.savefig('PNG_transparency_demonstration_1_retained.png')
