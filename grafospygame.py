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
agregarNodo=False
agregarArista=False





if __name__ == '__main__':
    pygame.init()
    reloj=pygame.time.Clock()
    ventana=pygame.display.set_mode([alto,ancho])

    imagen1=pygame.image.load("write.png")
    imagenNodo = pygame.transform.scale(imagen1, [20, 20])
    pygame.draw.circle(ventana,[255,0,0],(20,20),20)
    ventana.blit(imagenNodo, [10, 10])

    imagen2=pygame.image.load("arista.png")
    imagenArista = pygame.transform.scale(imagen2, [30,3])
    pygame.draw.circle(ventana,[255,0,0],(20,60),20)
    ventana.blit(imagenArista, [5, 58])
    

    while(fin==False):
    	for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

            if event.type== pygame.MOUSEBUTTONDOWN:
                print(event.button)

                if event.button==1:

                    if event.pos[0]<40 and event.pos[1]<40 and agregarNodo==False:
                        agregarNodo=True
                        agregarArista=False
                        pygame.draw.circle(ventana,[0,255,0],(20,20),20)
                        ventana.blit(imagenNodo, [10, 10])
                        pygame.draw.circle(ventana,[255,0,0],(20,60),20)
                        ventana.blit(imagenArista, [5, 58])

                    elif event.pos[0]<40 and event.pos[1]<40 and agregarNodo==True:
                         agregarNodo=False
                         pygame.draw.circle(ventana,[255,0,0],(20,20),20)
                         ventana.blit(imagenNodo, [10, 10])

                    elif event.pos[0]<40 and event.pos[1]>40 and event.pos[1]<80 and agregarArista==False:
                        agregarArista=True
                        agregarNodo=False
                        pygame.draw.circle(ventana,[0,255,0],(20,60),20)
                        ventana.blit(imagenArista, [5, 58])
                        pygame.draw.circle(ventana,[255,0,0],(20,20),20)
                        ventana.blit(imagenNodo, [10, 10])

                    elif event.pos[0]<40 and event.pos[1]>40 and event.pos[1]<80 and agregarArista==True:
                         agregarArista=False
                         pygame.draw.circle(ventana,[255,0,0],(20,60),20)
                         ventana.blit(imagenArista, [5, 68])
                         

                    elif (agregarNodo==True):
                        if len(nodos)==0:
                            nodos.append(event.pos)
                            pygame.draw.circle(ventana,azul,event.pos,20)
                        else:
                            cont=0
                            for nodo in nodos:
                                print(cont)
                                posicion=[]
                                posicion.append(event.pos[0]-nodo[0])
                                posicion.append(event.pos[1]-nodo[1])

                                if posicion[0]<0:
                                    posicion[0]=posicion[0]*(-1)
                                if posicion[1]<0:
                                    posicion[1]=posicion[1]*(-1)

                                Diferencia=(((posicion[0]**2) +(posicion[1]**2)))**0.5
                                print(Diferencia)
                                if Diferencia> 80:

                                    cont=cont+1
                            if len(nodos)==cont:
                                nodos.append(event.pos)
                                pygame.draw.circle(ventana,azul,event.pos,20)
                                    
                    elif (agregarArista==True):
                        for nodo in nodos:
                            posicion=[]
                            posicion.append(event.pos[0]-nodo[0])
                            posicion.append(event.pos[1]-nodo[1])

                            if posicion[0]<0:
                                posicion[0]=posicion[0]*(-1)
                            if posicion[1]<0:
                                posicion[1]=posicion[1]*(-1)
                            

                            Diferencia=(((posicion[0]**2) +(posicion[1]**2)))**0.5
                            if Diferencia< 20:
                                if nodo in aux:
                                    break
                                else:
                                    aux.append(nodo)

                                if (len(aux)==2):
                                    pygame.draw.line(ventana,azul,aux[0],aux[1])
                                    if aux in aristas or [aux[1],aux[0]] in aristas:
                                        continue
                                    else:
                                        aristas.append(aux)
                                        aristas.append([aux[1],aux[0]])
                                    aux=[]
                                break
                            

                    


                        

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
                        # Eliminar nodo
                        if Diferencia < 20 and borrar==True:
                            pygame.draw.circle(ventana,NEGRO,nodo,20)
                            nodos.remove(nodo)
                            
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
                    nodosConEtiqueta=[]
                    aristaConEtiquetas=[]


                    for nodo in nodos:
                        nodosConEtiqueta.append(chr(letraInicial))
                        pygame.draw.circle(ventana,azul,nodo,20)
                        fuente_J=pygame.font.Font(None,32)
                        mjs=chr(letraInicial)
                        info=fuente_J.render(mjs,True,NEGRO)
                        ventana.blit(info,nodo)
                        letraInicial+=1
                        
                    print(nodosConEtiqueta)
                    for arista in aristas:
                        v1=nodosConEtiqueta[nodos.index(arista[0])] 
                        v2=nodosConEtiqueta[nodos.index(arista[1])]
                        aristaConEtiquetas.append([v1,v2])
                    print(aristaConEtiquetas)


                if event.key == pygame.K_v:
                    nodoActual=nodos[0]
                    listaVisitada=[nodoActual]
                    trayectoria=[nodoActual]
                    pygame.draw.circle(ventana,[250,0,0],nodoActual,20)
                    pygame.display.flip()
                    print("los nodos", nodos)

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
