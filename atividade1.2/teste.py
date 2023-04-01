#A biblioteca PIL -> criar e tratar as imagens
#A biblioteca numpy -> manipular arrays

from PIL import Image
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
            
            
            #elimiando os valores negativos
            if soma < 0:
                soma = 0
            
            #limpando os valores que passaram de 255(valor max)
            if soma > 255:
                soma = 255
            
            #Atribuindo o valor do filtro em out na posição i e j
            out.putpixel((i,j),int(soma)) 

    return out


#Criando os filtros sobel 3x3
sobel_x = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]])

sobel_y = np.array([[1, 2,  1],
                    [0, 0,  0],
                    [-1,-2,-2]])


#Lendo uma imagem de um arquivo e transformando em escala de cinza
im = Image.open("imagem.jpg")
im = im.convert("L")

#Criando a imagem a e aplicando o filtro sobel_x em im
a = aplicar_filtro(sobel_x,im)

#Criando a imagem b e aplicando o filtro sobel_y em im
b = aplicar_filtro(sobel_y,im)

#imprimindo as imagens na tela
a.show()
b.show()
