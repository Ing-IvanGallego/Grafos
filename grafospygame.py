import pygame
import math
import random


def obtenerPosibleDestinio(nodoActual,aristas):
    posiblesDestinoNodoActual=[]
    for arista in aristas:
        if nodoActual==arista[0]:
            posiblesDestinoNodoActual.append(arista[1])
        else:
            continue
    return random.choice(posiblesDestinoNodoActual)

def nodoNoVisitado(lpd,aristas,listaVisitada):
    posiblesDestinoNodoActual=[]
    nodoDestino=[]
    for arista in aristas:
        if lpd==arista[0]:
            posiblesDestinoNodoActual.append(arista[1])
            if arista[1]  in listaVisitada:
                continue
            else:
                nodoDestino.append(arista[1])
                break
        else:
            continue
    print(len(nodoDestino))
    if len(nodoDestino)==0:
        print("ingres")
        return random.choice(posiblesDestinoNodoActual),False
    else:
        return nodoDestino[0],True






alto,ancho=1000,700
fin=False
azul = 255,255,255
NEGRO=0,0,0
nodos=[]
aristas=[]
aux=[]
borrar=False





if __name__ == '__main__':
    pygame.init()
    ventana=pygame.display.set_mode([alto,ancho])
    nods=pygame.sprite.Group()
    imagen=pygame.image.load("write.png")
    reloj=pygame.time.Clock()


    picture = pygame.transform.scale(imagen, [20, 20])
    pygame.draw.circle(ventana,[0,255,0],(20,20),20)
    ventana.blit(picture, [10, 10])
    

    while(fin==False):
    	for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

            if event.type== pygame.MOUSEBUTTONDOWN:
                print(event.button)

                if event.button==1:
                    if event.pos[0]<40 and event.pos[1]<40 and borrar==False:
                        borrar=True
                        pygame.draw.circle(ventana,[255,0,0],(20,20),20)
                        ventana.blit(picture, [10, 10])

                    elif event.pos[0]<40 and event.pos[1]<40 and borrar==True:
                         borrar=False
                         pygame.draw.circle(ventana,[0,255,0],(20,20),20)
                         ventana.blit(picture, [10, 10])
                         

                    elif (borrar==False):
                        nodos.append(event.pos)
                        pygame.draw.circle(ventana,azul,event.pos,20)
                        

                if event.button==3:
                    for nodo in nodos:
                        posicion=[]
                        posicion.append(event.pos[0]-nodo[0])
                        posicion.append(event.pos[1]-nodo[1])

                        if posicion[0]<0:
                            posicion[0]=posicion[0]*(-1)
                        if posicion[1]<0:
                            posicion[1]=posicion[1]*(-1)
                        

                        Diferencia=(((posicion[0]**2) +(posicion[1]**2)))**0.5
                        if Diferencia< 20 and borrar==False:
                            aux.append(nodo)
                            if (len(aux)==2):
                                pygame.draw.line(ventana,azul,aux[0],aux[1])
                                if aux in aristas or [aux[1],aux[0]] in aristas:
                                    print("ya esta")
                                else:
                                    aristas.append(aux)
                                    aristas.append([aux[1],aux[0]])
                                aux=[]
                            break

                        # Eliminar nodo
                        elif Diferencia < 20 and borrar==True:
                            pygame.draw.circle(ventana,NEGRO,nodo,20)
                            nodos.remove(nodo)
                            for arista in aristas:
                                if nodo == arista[0] or nodo == arista[1]:
                                    pygame.draw.line(ventana,NEGRO,arista[0],arista[1])
                                    
                                    aristas.remove(arista)
                    for arista in aristas:
                        pendiente=(arista[0][0]-arista[1][0])/(arista[0][1]-arista[1][1])
                        limiteinferior=pendiente-0.2
                        limiteSuperior=pendiente+0.2
                        pendiente2=(arista[0][0]-event.pos[0]+0.1)/(arista[0][1]-event.pos[1]+0.1)
                        if borrar==True and pendiente2>limiteinferior and pendiente2<limiteSuperior:
                            pygame.draw.line(ventana,NEGRO,arista[0],arista[1])
                            aristas.remove(arista)
                                    




            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    letraInicial=65

                    for nodo in nodos:
                        pygame.draw.circle(ventana,azul,nodo,20)
                        fuente_J=pygame.font.Font(None,32)
                        mjs=chr(letraInicial)
                        info=fuente_J.render(mjs,True,NEGRO)
                        ventana.blit(info,nodo)
                        letraInicial+=1
                        

                if event.key == pygame.K_v:
                    nodoActual=nodos[0]
                    listaVisitada=[nodoActual]
                    trayectoria=[nodoActual]
                    pygame.draw.circle(ventana,[250,0,0],nodoActual,20)
                    pygame.display.flip()

                    while len(listaVisitada) != len(nodos):
                        print(trayectoria)
                        pygame.time.delay(500)
                        lpd=obtenerPosibleDestinio(nodoActual,aristas)
                        trayectoria.append(lpd)

                        if lpd  in listaVisitada:
                            nodoActual=lpd
                            lpd,nuevo=nodoNoVisitado(lpd,aristas,listaVisitada)
                            trayectoria.append(lpd)
                            pygame.draw.line(ventana,[250,0,0],nodoActual,lpd)
                            print(lpd)
                            if nuevo==True:
                                pygame.draw.line(ventana,[250,0,0],nodoActual,lpd)
                                pygame.draw.circle(ventana,[250,0,0],lpd,20)
                                listaVisitada.append(lpd)
                                nodoActual=lpd
                                print("ingreso a nuevo")


                        else:
                            listaVisitada.append(lpd)
                            pygame.draw.circle(ventana,[250,0,0],lpd,20)
                            pygame.draw.line(ventana,[250,0,0],nodoActual,lpd)
                            nodoActual=lpd
                        pygame.display.flip()

                        






            
            pygame.display.flip()
