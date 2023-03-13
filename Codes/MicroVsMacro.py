import matplotlib.pyplot as plt
import numpy as np
N = 6

micro = (0.99, 0.80, 0.99, 1, 0.99, 0.99)

macro = (0.55, 0.58, 0.50, 0.5, 0.38, 0.20)

ind = np.arange(N)

# Figure size
plt.figure(figsize=(13, 6))

# Width of a bar
width = 0.3

# Plotting
plt.bar(ind, micro, width, label='Micro F1')
plt.bar(ind + width, macro, width, label='Macro F1')

plt.xlabel('Images from 1 to 20')
plt.ylabel('PSNR')
plt.title('Comparison of PSNR values of 20 images for AES and Triples DES algorithms')

images = ['BILSTM', 'CHAR-ATTENTION', 'BILSTM-CRF',
          'BILSTM-GLOVE', 'BILSTM-WORD2VEC', 'BILSTM-FASTEXT']

x = np.arange(0, len(images))
plt.xticks(x, images)

# Finding the best position for legends and putting it
plt.legend(loc='best')
plt.show()
