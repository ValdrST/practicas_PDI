import matplotlib.pyplot as plt
import numpy as np
from skimage import io
from skimage.color import convert_colorspace, rgb2gray
from PIL import Image

class ImagenProc():
    def __init__(self, img_file=''):
        self.img_file = img_file
        self.image = io.imread(self.img_file)/255.0
        self.color_space = Image.open(self.img_file).mode
        self.format = Image.open(self.img_file).format

        
    def get_datos(self):
        print("""
        nombre del archivo: {}
        tamaño:{}x{}
        tipo_imagen:{}
        color:{}
        """.format(
            self.img_file, 
            self.image.shape[0],
            self.image.shape[1],
            self.format,
            self.color_space
            )
        )
    
    def convert_colorspace(self, dest):
        try:
            if(dest != "GRAY"):
                self.image = convert_colorspace(self.image, self.color_space, dest)
                self.color_space = dest
            else:
                self.image = rgb2gray(self.image)
            
        except Exception as e:
            print(e,"Espacio de color de destino no valido")

    def get_RGB_components(self):
        image_red = np.copy(self.image)
        image_red[:,:,1] = 0
        image_red[:,:,2] = 0
        image_green = np.copy(self.image)
        image_green[:,:,0] = 0
        image_green[:,:,2] = 0
        image_blue = np.copy(self.image)
        image_blue[:,:,0] = 0
        image_blue[:,:,1] = 0
        return (image_red, image_green, image_blue)

    def crop_image(self, x1, y1, x2, y2):
        self.image = self.image[y1:y2, x1:x2]

    def show_image(self, show_color_canal = False, title_orig = "Imagen original", show = True, gray = False):
        plt.figure()
        plt.title(title_orig)
        if(gray):
            plt.imshow(self.image,cmap=plt.cm.gray)
        else:
            plt.imshow(self.image)
        if(show_color_canal):
            rgb_image = self.get_RGB_components()
            plt.figure()
            plt.title("Canal rojo")
            plt.imshow(rgb_image[0])
            plt.figure()
            plt.title("Canal verde")
            plt.imshow(rgb_image[1])
            plt.figure()
            plt.title("Canal azul")
            plt.imshow(rgb_image[2])
        if(show):
            plt.show()
