import cv2
import numpy as np
#cv2 => görüntü işleme
#numpy => çok boyutlu diziler ve matematiksel işlemler

def read_pgm(filename):
    return cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
#cv2.IMREAD_GRAYSCALE görüntüyü doğrudan gri tonlamalı okumasını sağlar
#pgm dosyasını okur

def sobel(image):
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    
    magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
    magnitude = np.clip(magnitude, 0, 255).astype(np.uint8)
    #np.uint8 => unsigned integer (data type)
    
    return magnitude
#cv2.CV_64F sabiti, Sobel filtresinin hesaplamalarında 
#64-bit float veri türünü kullanacağını belirtiyor.

def write_pgm(filename, image):
    cv2.imwrite(filename, image)
#sonuç görüntüsünü pgm formatında kaydeder.

if __name__ == "__main__":
    input_filename = "lena.pgm"
    output_filename = "outputsobel.pgm"

    input_image = read_pgm(input_filename)
    
    sobel_edges = sobel(input_image)

    write_pgm(output_filename, sobel_edges)


    print("Basariyla kaydedildi:", output_filename)

