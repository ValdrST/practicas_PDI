from MTF import MTF
import numpy as np

if __name__ == '__main__':
    mtf = MTF()
    estimulo_visual = mtf.generar_estimpulo_visual(contraste_offset=4.0, fx_offset=2+np.pi, size=4096)
    mtf.show_data(estimulo_visual)
