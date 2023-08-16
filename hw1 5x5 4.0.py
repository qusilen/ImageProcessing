import cv2
import numpy as np
#cv2 => görüntü işleme
#numpy => çok boyutlu diziler ve matematiksel işlemler

def read_pgm(filename):
    return cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
#cv2.IMREAD_GRAYSCALE görüntüyü doğrudan gri tonlamalı okumasını sağlar
#pgm dosyasını okur

def convolution(image, kernel):
    return cv2.filter2D(image, -1, kernel)
#görüntü ve kernel matrisi arasında konvolüsyon işlemini gerçekleştirir
#-1 => kanal indeksi / giriş görüntüsünde renk kanallarını korumak için

def write_pgm(filename, image):
    cv2.imwrite(filename, image)
#sonuç görüntüsünü pgm formatında kaydeder.

if __name__ == "__main__":
    input_filename = "lena.pgm"
    output_filename = "output5x54.0.pgm"

    kernel_size = 5
    kernel_values = np.array([
        [0.0037, 0.0101, 0.0183, 0.0101, 0.0037],
        [0.0101, 0.0276, 0.0498, 0.0276, 0.0101],
        [0.0183, 0.0498, 0.0901, 0.0498, 0.0183],
        [0.0101, 0.0276, 0.0498, 0.0276, 0.0101],
        [0.0037, 0.0101, 0.0183, 0.0101, 0.0037]


    ])

    input_image = read_pgm(input_filename)
    kernel = np.array(kernel_values, dtype=np.float32)
    
    convolved_image = convolution(input_image, kernel)

    write_pgm(output_filename, convolved_image)

    print("Basariyla kaydedildi:", output_filename)

