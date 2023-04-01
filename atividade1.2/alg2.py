#A biblioteca PIL -> criar e tratar as imagens
#A biblioteca numpy -> manipular arrays

from PIL import Image, ImageFilter
import numpy as np


#recebe um kernel 3x3 (filtro) e aplica ele em uma imagem e retorna uma copia da imagem com filtro aplicado
def aplicar_filtro(kernel, im):

    #pegando as dimensões da imagem
    x,y = im.size

    #Criando uma imagem na escala de cinza com as mesmas dimensões que im
    out = Image.new("L", (x,y))
    
    #Visitando cada pixel de out para atribuir valor
    for j in range(y):
        for i in range(x):

            soma = 0

            for xkernel in range(3):
                for ykernel in range(3):
                    
                    #Checando os problemas de borda da imagem im
                    if i-1+xkernel < 0 or i-1+xkernel >= x or j-1+ykernel < 0 or j-1+ykernel >= y:
                        soma = soma + 0

                    #Caso a coordenada esteja dentro de im, então aquele ponto é calculado
                    else:
                        soma = soma + im.getpixel((i - 1 + xkernel, j - 1 + ykernel)) * kernel[xkernel][ykernel] * 1/4
            
           #Atribuindo o valor do filtro em out na posição i e j
            out.putpixel((i,j),int(soma)) 

    return out

def imagem_b(im):
    x,y = im.size
    b = Image.new("L", (x,y))

    for i in range(x):
        for j in range(y):
            if im.getpixel((i,j)) > 0:
                b.putpixel((i,j), 255)

    return b



#-------MAIN-------#

#Criando os filtros Laplace
laplace = np.array([[0,-1,0],
                    [-1,4,-1],
                    [0,-1,0]])

#Lendo imagem e convertendo para grayscale
im_original = Image.open("imagem.jpg")
im_original = im_original.convert("L")

"""
x,y = 500,500
#Criando uma imagem com dimensões x e y com todos os pixels brancos 
im_original = Image.new("L", (500,500), 255)

#Todas as bordas terão preto
for i in range(500):
    im_original.putpixel((i,0), 0)
    im_original.putpixel((i, y-1), 0)
    im_original.putpixel((0,1), 0)
    im_original.putpixel((x-1, i), 0)
"""

im = im_original.filter(ImageFilter.GaussianBlur(2))


#Criando a imagem a e aplicando o filtro em im
a = aplicar_filtro(laplace,im)

b = imagem_b(a)

b.show()
