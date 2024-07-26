## This is course material for Introduction to Python Scientific Programming
## Example code: matplotlib_basic_plot.py
## Author: Allen Y. Yang
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import matplotlib.pyplot as plt
import numpy as np

# generate a basic sample point array on x-axis
x = np.arange(0,2*np.pi,0.1)

# Create a sin function sample
y0 = np.sin(x)
plt.plot(x, y0, color = 'r', linewidth = 3)

# Create a dash cos function sample
y1 = np.cos(x)
plt.plot(x, y1, 'b--', linewidth = 1)
plt.ylim(-1, 1)
plt.xlim(0,2*np.pi)
plt.xticks(np.arange(0,2*np.pi,np.pi/4), ['0', 'pi/4', 'pi/2', '3pi/4', 'pi', '5pi/4', '3pi/2', '7pi/4'])
plt.show()

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Load the Lenna image and national flag image
lenna_image_path = 'path_to_lenna_image.png'  # Replace with the actual path to Lenna image
flag_image_path = 'path_to_flag_image.png'    # Replace with the actual path to flag image

lenna_image = Image.open(lenna_image_path)
flag_image = Image.open(flag_image_path)

# Convert images to NumPy arrays
lenna_array = np.array(lenna_image)
flag_array = np.array(flag_image)

# Get dimensions of the flag image
flag_height, flag_width, _ = flag_array.shape

# Replace the top right corner of the Lenna image with the flag image
lenna_array[0:flag_height, -flag_width:] = flag_array

# Convert back to Image and display
modified_lenna_image = Image.fromarray(lenna_array)
plt.imshow(modified_lenna_image)
plt.axis('off')
plt.show()
