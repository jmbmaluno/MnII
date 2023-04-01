from PIL import Image
import numpy as np


def aplicar_filtro(kernel, im):
    x,y = im.size
    px_im = im.load()

    out = Image.new("L", (x,y))
    
    for j in range(y):
        for i in range(x):
            soma = 0

            for xkernel in range(3):
                for ykernel in range(3):
                    if i-1+xkernel < 0 or i-1+xkernel >= x or j-1+ykernel < 0 or j-1+ykernel >= y:
                        soma = soma + 0
                    else:
                        soma = soma + im.getpixel((i - 1 + xkernel, j - 1 + ykernel)) * kernel[xkernel][ykernel]
            

            if soma < 0:
                soma = 0
            if soma > 255:
                soma = 255
            
            out.putpixel((i,j),int(soma)) 

    return out


sobel_x = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]])

sobel_y = np.array([[1, 2,  1],
                    [0, 0,  0],
                    [-1,-2,-2]])


im = Image.open("imagem.jpg")
im = im.convert("L")


a = aplicar_filtro(sobel_x,im)
b = aplicar_filtro(sobel_y,im)

a.show()
b.show()
