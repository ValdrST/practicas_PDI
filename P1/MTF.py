import scipy as sc
import numpy as np
import math
import matplotlib.pyplot as plt
class MTF(object):
    def __init__(self, *args):
        self.frecuencias = []
    
    def generar_estimpulo_visual(self,contraste_offset=4.0, fx_offset=2.0, size=8096):
        # Se inicia matriz de 4000x4000
        arr =  np.zeros((size,size))
        # Se inicia arreglod de 4000
        arrx = np.zeros((size))

        sampleRate = size
        # Se calculan los pasos para la funcion 10^n
        f_x10 = np.arange(0,fx_offset,fx_offset/size)
        # Se calculan los pasos para la funcion 10^n
        c_x10 = np.arange(contraste_offset*-1,0,contraste_offset/size)
        length = 1
        t = np.linspace(0, length, sampleRate * length)
        # Se calcula el barrido de frecuencias
        for x, tt in enumerate(t):
            if(x == size):
                break
            # Se usa la funcion 10^x para calcular la frecuencia
            frecuencia = math.exp(f_x10[x])
            self.frecuencias.append(frecuencia)
            # se genera el arreglo que sera la funcion seno
            arrx[x] = np.sin((2*np.pi*frecuencia* tt))*127
        

        for y in range(0,size,1):
            # Se usa la funcion 10^y para calcular el contraste
            contraste = math.pow(10,c_x10[y])
            # se multiplica cada renglon por el contraste calculado [0,1]
            arr[y] = contraste * arrx
        return arr
    
    def onclick(self,event):
        #print(event)
        #print("{0}, {1},".format(event.xdata, event.ydata))
        f = self.frecuencias[int(event.xdata)]
        print("{:.2f}[Hz]".format(round(f,2)))
    
    def show_data(self, data):
        fig = plt.figure()
        cid = fig.canvas.mpl_connect('button_press_event', self.onclick)
        plt.rcParams['image.cmap'] = 'gray'
        plt.imshow(data+127, vmin=0, vmax=255.0)
        plt.show()
