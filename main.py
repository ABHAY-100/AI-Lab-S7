import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("image.png", 0)

rows = np.array_split(image, 2, axis=0)

k=1

for row in rows:
    cols = np.array_split(row, 4, axis=1)
    for part in cols:
        plt.subplot(2, 8, k)
        plt.imshow(part, cmap="gray")
        k=k+1

        plt.subplot(2, 8, k)
        plt.hist(part.ravel(), 256)
        k=k+1

plt.show()