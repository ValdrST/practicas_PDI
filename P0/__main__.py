from ImagenProc import ImagenProc
if __name__ == '__main__':
    imp = ImagenProc("imagenes2/magriclonRGB.jpg")
    
    imp_retina = ImagenProc("imagenes2/retinaRGB.jpg")
    imp_retina_orig = ImagenProc("imagenes2/retinaRGB.jpg")
    imp_corte_bmp = ImagenProc("imagenes2/corte.bmp")
    imp_corte_bmp_orig = ImagenProc("imagenes2/corte.bmp")

    imp.get_datos()
    imp.show_image(title_orig="Imagen Original", show_color_canal=True, show=False)
    
    imp_retina.get_datos()
    imp_retina.show_image(title_orig="Imagen Original", show=False)
    imp_retina.convert_colorspace('GRAY')
    imp_retina.show_image(title_orig="Imagen escala grises", gray=True, show=False)
    imp_retina = imp_retina_orig
    imp_retina.convert_colorspace('HSV')
    imp_retina.show_image(title_orig="Imagen HSV", show=False)
    imp_retina = imp_retina_orig
    imp_retina.convert_colorspace('YUV')
    imp_retina.show_image(title_orig="Imagen YUV", show=False)
    imp_retina = imp_retina_orig

    imp_corte_bmp.get_datos()
    imp_corte_bmp.show_image(title_orig="Corte original", show=False)
    imp_corte_bmp.crop_image(137,163,412,502)
    imp_corte_bmp.get_datos()
    imp_corte_bmp.show_image(title_orig="Corte 1/3 de su tamaño", show=False)
    imp_corte_bmp = imp_corte_bmp_orig
    imp_corte_bmp.crop_image(100, 100, 300,350)
    imp_corte_bmp.get_datos()
    imp_corte_bmp.show_image(title_orig="Corte lugar centrico")
