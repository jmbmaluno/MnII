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
                        soma = soma + im.getpixel((i - 1 + xkernel, j - 1 + ykernel)) * kernel[xkernel][ykernel]
            
           #Atribuindo o valor do filtro em out na posição i e j
            out.putpixel((i,j),int(soma)) 

    return out

#Elevando ao quadrado cada valor da imagem a
def elevar_ao_quadrado(a):
    x,y = a.size

    for i in range(x):
        for j in range(y):
            k = a.getpixel((i,j))

            a.putpixel((i,j), int(k*k))


#Cria uma imagem C que é a soma de A e B
def somar_imagens(a,b):
    x,y = a.size
    c = Image.new("L", (x,y))

    for i in range(x):
        for j in range(y):
            valor = a.getpixel((i,j)) + b.getpixel((i,j))
            c.putpixel((i,j), int(valor))
    
    return c

#Todo valor que for maior que ts será 1 (255)
#Todo valor que for menor que ts será 0 (0)
def aplicar_threshold(im,ts):
    x,y = im.size
    d = Image.new("L", (x,y))

    for i in range(x):
        for j in range(y):
            if im.getpixel((i,j)) > ts*255:
                d.putpixel((i,j), 255)

    return d



#-------MAIN-------#

#Criando os filtros sobel 3x3
sobel_x = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]])

sobel_y = np.array([[1, 2,  1],
                    [0, 0,  0],
                    [-1,-2,-2]])


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


#Criando a imagem a e aplicando o filtro sobel_x em im
a = aplicar_filtro(sobel_x,im)
#Criando a imagem b e aplicando o filtro sobel_y em im
b = aplicar_filtro(sobel_y,im)

elevar_ao_quadrado(a)
elevar_ao_quadrado(b)


c = somar_imagens(a,b)


d = aplicar_threshold(c,0.5)

d.show()
