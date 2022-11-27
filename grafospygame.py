import pygame
import networkx as nx
import numpy as np 
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
    if len(nodoDestino)==0:
        return random.choice(posiblesDestinoNodoActual),False
    else:
        return nodoDestino[0],True

def camino(g, inicio, fin, visitados = None):
    vertices = g[0]
    aristas = g[1]

    if not visitados:
        visitados = []

    visitados.append(inicio)
    if inicio == fin:
        return visitados
    ''' Seleccionar todas las aristas que contengan x como primer elemento y que no hayan sido visitadas '''
    seleccion = [x for x in aristas if x[0] == inicio and x[1] not in visitados]
    resultado = []
    for arista in seleccion:
        ''' Probar cada vertice conectado con el actual '''
        if resultado := camino(g, arista[1], fin, visitados):
            break
    else:
        ''' Ninguno de los vertices conectados lleva a destino '''
        visitados.pop()

    return resultado

def obtenerRutas(nodos):
    arista=[]
    for nodo in nodos[1:]:
        if arista==[]: arista.append([nodos[0],nodo])
        else: arista.append([arista[len(arista)-1][1],nodo])
    return arista

def actualizar(nodos,aristas):
    letraInicial=65
    nodosConEtiqueta=[]
    aristaConEtiquetas=[]
    for nodo in nodos:
        nodosConEtiqueta.append(chr(letraInicial))
        pygame.draw.circle(ventana,BLANCO,nodo,20)
        fuente_J=pygame.font.Font(None,32)
        mjs=chr(letraInicial)
        info=fuente_J.render(mjs,True,NEGRO)
        ventana.blit(info,nodo)
        letraInicial+=1
    for arista in aristas:
        v1=nodosConEtiqueta[nodos.index(arista[0])] 
        v2=nodosConEtiqueta[nodos.index(arista[1])]
        aristaConEtiquetas.append([v1,v2])
        pygame.draw.line(ventana,BLANCO,arista[0],arista[1])
    return nodosConEtiqueta,aristaConEtiquetas 


def esEuleriano(nodos, edges):
    euleriana=True
    vecinos=[0]*len(nodos)
    for (nodoinicio,nodoFinal) in edges:
        vecinos[nodos.index(nodoinicio)]+=1
        vecinos[nodos.index(nodoFinal)]+=1
    for vecinoNodo in vecinos:
        if (vecinoNodo%2==1 or vecinoNodo==0):
            euleriana=False
            return euleriana,nodos[vecinos.index(vecinoNodo)]
            break
    return euleriana

def circuitoHamiltoniano(edges,nodos):
    curr_path=[0]
    circuit=[]
    circuitoConEtiqueta=[]
    vecinos=[[] for _ in range(len(nodos))]
    for (nodoinicio,nodoFinal) in edges:
        vecinos[nodos.index(nodoinicio)].append(nodos.index(nodoFinal))
    while(curr_path):
        curr_v=curr_path[-1]
        if vecinos[curr_v]:
            nextv=vecinos[curr_v].pop()
            curr_path.append(nextv)
        else:
            circuit.append(curr_path.pop())
    for  nodo in circuit:
        circuitoConEtiqueta.append(nodos[nodo])
    return circuitoConEtiqueta

def recorrerNodos(nodos,v,visitados,vecinos):
    visitados[nodos.index(v)]=True
    for u in vecinos[nodos.index(v)]:
        if not visitados[nodos.index(u)]:
            recorrerNodos(nodos,u,visitados,vecinos)
    
def isconexo(nodos,edges):
    visitados=[]
    for i in range(len(nodos)):
        visitados.append(False)
    respuesta=True
    vecinos=[[] for _ in range(len(nodos))]
    for (nodoinicio,nodoFinal) in edges:
        vecinos[nodos.index(nodoinicio)].append(nodoFinal)
        vecinos[nodos.index(nodoFinal)].append(nodoinicio)

    if ([] in vecinos):
        return False
    else:
        casa=recorrerNodos(nodos,nodos[0],visitados,vecinos)
        for nodovisitado in visitados:
            if not nodovisitado:
                respuesta=False
        return respuesta

def asignacionGrupo(nodos,vecinos,visitados,cualGrupo,grupos):
     while all(visitados)==False:
         for u in grupos[cualGrupo]:
             if visitados[nodos.index(u)]==False:
                 visitados[nodos.index(u)] = True
                 if cualGrupo==1: grupo=0
                 else: grupo=1
                 for nodo in vecinos[nodos.index(u)]:
                     if not nodo in grupos[grupo]:
                         grupos[grupo].append(nodo)
                     else: continue
             else:
                 continue
         cualGrupo=grupo

def isBiopartido(nodos,edges):
     respuesta=True
     grupo=[False]*len(nodos)
     visitados=[False]*len(nodos)
     vecinos=[[] for _ in range(len(nodos))]
     for (nodoinicio,nodoFinal) in edges:
        vecinos[nodos.index(nodoinicio)].append(nodoFinal)
        vecinos[nodos.index(nodoFinal)].append(nodoinicio)
     visitados[0]=True
     grupos=[[],[]]
     grupos[0].append(nodos[0])
     for nodogrupo1 in vecinos[0]:
        grupos[1].append(nodogrupo1)
     asignacionGrupo(nodos,vecinos,visitados,1,grupos)
     if set(grupos[0]) & set(grupos[1]):
        return False
     else:
        return True
def colorearMapa(nodos,edges):
    colorNodos=[""]*len(nodos)
    vecinos=[[] for _ in range(len(nodos))]

    for (nodoinicio,nodoFinal) in edges:
        vecinos[nodos.index(nodoinicio)].append(nodoFinal)
        if digraph==True:
            if nodoinicio in vecinos[nodos.index(nodoFinal)]:
                continue
            else:
                vecinos[nodos.index(nodoFinal)].append(nodoinicio)
    
    for indexNodo in range(len(nodos)):
        verificarColores=[AMARILLO,VERDE,ROJO,AZUL,[0,255,255]]
        for vecino in vecinos[indexNodo]:
            if colorNodos[nodos.index(vecino)] in verificarColores:
                verificarColores.remove(colorNodos[nodos.index(vecino)])

        colorNodos[indexNodo]=verificarColores[0]
        
    return colorNodos

alto,ancho=700,1200
fin=False
BLANCO = 255,255,255
NEGRO=0,0,0
ROJO=[255,0,0]
AZUL=[0,0,255]
VERDE=[0,255,0]
AMARILLO=[255,255,0]
G=nx.DiGraph()
nodos=[]
aristas=[]
aux=[]
NodosInicioFinal=[]
borrar=False
agregarNodo=False
agregarArista=False
visitar=False
conexo=False
euleriano=False
bipartito=False
colorearGrafo=False
mostrar_menu = True

digraph=False
imgMenu = pygame.image.load('graphMenu.png')

if __name__ == '__main__':
    pygame.init()
    reloj=pygame.time.Clock()
    ventana=pygame.display.set_mode([ancho,alto])
#Menu to select digraphs and undirected graphs
    while mostrar_menu:
        accion=pygame.mouse.get_pos()
        if (accion[0] > 350 and accion[0] < 503 and accion[1] > 467 and accion[1] < 529):
            pygame.draw.rect(ventana,ROJO,(328,450,160,80),2,50)
                         
        if (accion[0] > 694 and accion[0] < 858 and accion[1] > 467 and accion[1] < 529):
            pygame.draw.rect(ventana,ROJO,(670,450,210,80),2,50)      
                                   
        for event in pygame.event.get():
            ventana.blit(imgMenu, (200,0)) 
            if event.type == pygame.QUIT:
                mostrar_menu=False

            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos() #Gets the mouse position
                if event.button == 1:
                    if (position[0] > 350 and position[0] < 503 and
                                    position[1] > 467 and position[1] < 529):
                                    # Digraph
                                    digraph = True
                                    mostrar_menu = False
                                    mjs="DIGRAPH"
                                    fin=True

                    elif (position[0] > 694 and position[0] < 858 and
                                    position[1] > 467 and position[1] < 529):
                                    #Undirected
                                    digraph = False
                                    mostrar_menu = False
                                    mjs="UNDIRECTED"
                                    fin=True
        pygame.display.update()
    
    pygame.draw.rect(ventana, NEGRO, (0,0,ancho,alto))
    fuente_texto=pygame.font.Font(None,25)
    info=fuente_texto.render(mjs,True,BLANCO)
    ventana.blit(info,[45,10])
    imagen1=pygame.image.load("write.png")
    imagenNodo = pygame.transform.scale(imagen1, [20, 20])
    pygame.draw.circle(ventana,ROJO,(20,20),20)
    ventana.blit(imagenNodo, [10, 10])

    imagen2=pygame.image.load("arista.png")
    imagenArista = pygame.transform.scale(imagen2, [30,3])
    pygame.draw.circle(ventana,ROJO,(20,60),20)
    ventana.blit(imagenArista, [5, 58])
    
    imagen3=pygame.image.load("visitas.png")
    imagenvisitar = pygame.transform.scale(imagen3, [30, 30])
    pygame.draw.circle(ventana,ROJO,(20,100),20)
    ventana.blit(imagenvisitar, [5, 80])

    imagen4=pygame.image.load("flecha.png")
    imagenflecha = imagen4

    imagen6=pygame.image.load("flechaBorrar.png")
    imagenflechaBorrar = imagen6

    iconoConexo="C"
    fuente_J=pygame.font.Font(None,32)
    pygame.draw.circle(ventana,ROJO,(20,140),20)
    info=fuente_J.render(iconoConexo,True,NEGRO)
    ventana.blit(info,[15,135])

    imagen5=pygame.image.load("b.png")
    imagenbipartido= pygame.transform.scale(imagen5, [30, 30])
    pygame.draw.circle(ventana,ROJO,(20,180),20)
    ventana.blit(imagenbipartido, [5, 170])

    iconoEuleriano="E"
    fuente_J=pygame.font.Font(None,32)
    pygame.draw.circle(ventana,ROJO,(20,220),20)
    info=fuente_J.render(iconoEuleriano,True,NEGRO)
    ventana.blit(info,[15,213])

    imagen_Mouse=pygame.image.load("Mouse.png")
    imgMouseDerecho= pygame.transform.scale(imagen_Mouse, [30, 30])
    imgMouseIzquierda = pygame.transform.flip(imgMouseDerecho, True, False)

    while(fin==True):

    	for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=False

            if event.type== pygame.MOUSEBUTTONDOWN:

                if event.button==1:
                    #Boton de agregar nodo
                        #Activacion
                    if event.pos[0]<40 and event.pos[1]<40 and agregarNodo==False:
                        agregarNodo=True
                        agregarArista=False
                        visitar=False
                        euleriano=False
                        conexo=False
                        bipartito=False
                        colorearGrafo=False
                        pygame.draw.circle(ventana,VERDE,(20,20),20)
                        ventana.blit(imagenNodo, [10, 10])
                        pygame.draw.circle(ventana,ROJO,(20,60),20)
                        ventana.blit(imagenArista, [5, 58])
                        pygame.draw.circle(ventana,ROJO,(20,100),20)
                        ventana.blit(imagenvisitar, [5, 80])
                        pygame.draw.circle(ventana,ROJO,(20,140),20)
                        info=fuente_J.render(iconoConexo,True,NEGRO)
                        ventana.blit(info,[15,135])
                        pygame.draw.circle(ventana,ROJO,(20,180),20)
                        ventana.blit(imagenbipartido, [5, 170])
                        pygame.draw.circle(ventana,ROJO,(20,220),20)
                        info=fuente_J.render(iconoEuleriano,True,NEGRO)
                        ventana.blit(info,[15,213])

                        #Desactivacion
                    elif event.pos[0]<40 and event.pos[1]<40 and agregarNodo==True:
                         agregarNodo=False
                         pygame.draw.circle(ventana,ROJO,(20,20),20)
                         ventana.blit(imagenNodo, [10, 10])

                    #Boton agregar arista
                    elif event.pos[0]<40 and event.pos[1]>40 and event.pos[1]<80 and agregarArista==False:
                        agregarArista=True
                        agregarNodo=False
                        visitar=False
                        bipartito=False
                        conexo=False
                        euleriano=False
                        colorearGrafo=False
                        pygame.draw.circle(ventana,VERDE,(20,60),20)
                        ventana.blit(imagenArista, [5, 58])
                        pygame.draw.circle(ventana,ROJO,(20,20),20)
                        ventana.blit(imagenNodo, [10, 10])
                        pygame.draw.circle(ventana,ROJO,(20,100),20)
                        ventana.blit(imagenvisitar, [5, 80])
                        pygame.draw.circle(ventana,ROJO,(20,140),20)
                        info=fuente_J.render(iconoConexo,True,NEGRO)
                        ventana.blit(info,[15,135])
                        pygame.draw.circle(ventana,ROJO,(20,180),20)
                        ventana.blit(imagenbipartido, [5, 170])
                        pygame.draw.circle(ventana,ROJO,(20,220),20)
                        info=fuente_J.render(iconoEuleriano,True,NEGRO)
                        ventana.blit(info,[15,213])

                    elif event.pos[0]<40 and event.pos[1]>40 and event.pos[1]<80 and agregarArista==True:
                         agregarArista=False
                         pygame.draw.circle(ventana,ROJO,(20,60),20)
                         ventana.blit(imagenArista, [5, 68])
                    #Boton hacer visitar
                    elif event.pos[0]<40 and event.pos[1]>80 and event.pos[1]<120 and visitar==False:
                        agregarArista=False
                        agregarNodo=False
                        visitar=True
                        conexo=False
                        euleriano=False
                        bipartito=False
                        colorearGrafo=False
                        pygame.draw.circle(ventana,ROJO,(20,60),20)
                        ventana.blit(imagenArista, [5, 58])
                        pygame.draw.circle(ventana,ROJO,(20,20),20)
                        ventana.blit(imagenNodo, [10, 10])
                        pygame.draw.circle(ventana,VERDE,(20,100),20)
                        ventana.blit(imagenvisitar, [5, 80])
                        pygame.draw.circle(ventana,ROJO,(20,140),20)
                        info=fuente_J.render(iconoConexo,True,NEGRO)
                        ventana.blit(info,[15,135])
                        pygame.draw.circle(ventana,ROJO,(20,180),20)
                        ventana.blit(imagenbipartido, [5, 170])
                        pygame.draw.circle(ventana,ROJO,(20,220),20)
                        info=fuente_J.render(iconoEuleriano,True,NEGRO)
                        ventana.blit(info,[15,213])

                    elif event.pos[0]<40 and event.pos[1]>80 and event.pos[1]<120 and visitar==True:
                         visitar=False
                         pygame.draw.circle(ventana,ROJO,(20,100),20)
                         ventana.blit(imagenvisitar, [5, 80])

                    #Boton saber si es conexo
                    elif event.pos[0]<40 and event.pos[1]>120 and event.pos[1]<160 and conexo==False:
                        agregarArista=False
                        agregarNodo=False
                        visitar=False
                        conexo=True
                        euleriano=False
                        bipartito=False
                        colorearGrafo=False
                        pygame.draw.rect(ventana, NEGRO, [200,6,800,30])
                        mjs="¿Tu grafo sera conexo?"
                        fuente_texto=pygame.font.Font(None,25)
                        info=fuente_texto.render(mjs,True,BLANCO)
                        ventana.blit(info,[500,8])

                        pygame.draw.circle(ventana,ROJO,(20,60),20)
                        ventana.blit(imagenArista, [5, 58])
                        pygame.draw.circle(ventana,ROJO,(20,20),20)
                        ventana.blit(imagenNodo, [10, 10])
                        pygame.draw.circle(ventana,ROJO,(20,100),20)
                        ventana.blit(imagenvisitar, [5, 80])
                        pygame.draw.circle(ventana,VERDE,(20,140),20)
                        info=fuente_J.render(iconoConexo,True,NEGRO)
                        ventana.blit(info,[15,135])
                        pygame.draw.circle(ventana,ROJO,(20,180),20)
                        ventana.blit(imagenbipartido, [5, 170])
                        pygame.draw.circle(ventana,ROJO,(20,220),20)
                        info=fuente_J.render(iconoEuleriano,True,NEGRO)
                        ventana.blit(info,[15,213])

                    elif event.pos[0]<40 and event.pos[1]>120 and event.pos[1]<160 and conexo==True:
                         conexo=False
                         pygame.draw.circle(ventana,ROJO,(20,140),20)
                         info=fuente_J.render(iconoConexo,True,NEGRO)
                         ventana.blit(info,[15,135])
                    #Boton saber si es bipartito
                    elif event.pos[0]<40 and event.pos[1]>160 and event.pos[1]<200 and bipartito==False:
                        agregarArista=False
                        agregarNodo=False
                        visitar=False
                        conexo=False
                        euleriano=False
                        bipartito=True
                        colorearGrafo=False
                        pygame.draw.rect(ventana, NEGRO, [200,6,800,30])
                        mjs="¿Tu grafo sera bipartito?"
                        fuente_texto=pygame.font.Font(None,25)
                        info=fuente_texto.render(mjs,True,BLANCO)
                        ventana.blit(info,[500,8])
                        pygame.draw.circle(ventana,ROJO,(20,60),20)
                        ventana.blit(imagenArista, [5, 58])
                        pygame.draw.circle(ventana,ROJO,(20,20),20)
                        ventana.blit(imagenNodo, [10, 10])
                        pygame.draw.circle(ventana,ROJO,(20,100),20)
                        ventana.blit(imagenvisitar, [5, 80])
                        pygame.draw.circle(ventana,ROJO,(20,140),20)
                        info=fuente_J.render(iconoConexo,True,NEGRO)
                        ventana.blit(info,[15,135])
                        pygame.draw.circle(ventana,VERDE,(20,180),20)
                        ventana.blit(imagenbipartido, [5, 170])
                        pygame.draw.circle(ventana,ROJO,(20,220),20)
                        info=fuente_J.render(iconoEuleriano,True,NEGRO)
                        ventana.blit(info,[15,213])
                    elif event.pos[0]<40 and event.pos[1]>160 and event.pos[1]<200 and bipartito==True:
                        bipartito=False
                        pygame.draw.circle(ventana,ROJO,(20,180),20)
                        ventana.blit(imagenbipartido, [5, 170])
                    #boton si es euleriano
                    elif event.pos[0]<40 and event.pos[1]>200 and event.pos[1]<240 and euleriano==False:
                        agregarArista=False
                        agregarNodo=False
                        visitar=False
                        conexo=False
                        euleriano=True
                        bipartito=False
                        colorearGrafo=False
                        pygame.draw.rect(ventana, NEGRO, [200,6,700,30])
                        mjs="¿Tu grafo sera Euleriano?"
                        fuente_texto=pygame.font.Font(None,25)
                        info=fuente_texto.render(mjs,True,BLANCO)
                        ventana.blit(info,[500,8])
                        pygame.draw.circle(ventana,ROJO,(20,60),20)
                        ventana.blit(imagenArista, [5, 58])
                        pygame.draw.circle(ventana,ROJO,(20,20),20)
                        ventana.blit(imagenNodo, [10, 10])
                        pygame.draw.circle(ventana,ROJO,(20,100),20)
                        ventana.blit(imagenvisitar, [5, 80])
                        pygame.draw.circle(ventana,ROJO,(20,140),20)
                        info=fuente_J.render(iconoConexo,True,NEGRO)
                        ventana.blit(info,[15,135])
                        pygame.draw.circle(ventana,ROJO,(20,180),20)
                        ventana.blit(imagenbipartido, [5, 170])
                        pygame.draw.circle(ventana,VERDE,(20,220),20)
                        info=fuente_J.render(iconoEuleriano,True,NEGRO)
                        ventana.blit(info,[15,213])

                    elif event.pos[0]<40 and event.pos[1]>200 and event.pos[1]<240 and euleriano==True:
                        euleriano=False
                        pygame.draw.circle(ventana,ROJO,(20,220),20)
                        info=fuente_J.render(iconoEuleriano,True,NEGRO)
                        ventana.blit(info,[15,213])
 ####################################################################################      
                    #Logica de los botones                        
                    elif (agregarNodo==True and event.pos[1] >60):
                        if len(nodos)==0:
                            nodos.append(event.pos)
                            pygame.draw.circle(ventana,BLANCO,event.pos,20)
                        else:
                            cont=0
                            for nodo in nodos:
                    
                                posicion=[]
                                posicion.append(event.pos[0]-nodo[0])
                                posicion.append(event.pos[1]-nodo[1])
                                if posicion[0]<0:
                                    posicion[0]=posicion[0]*(-1)
                                if posicion[1]<0:
                                    posicion[1]=posicion[1]*(-1)
                                Diferencia=(((posicion[0]**2) +(posicion[1]**2)))**0.5
                                if Diferencia> 80:
                                    cont=cont+1
                            if len(nodos)==cont:
                                nodos.append(event.pos)
                                pygame.draw.circle(ventana,BLANCO,event.pos,20)
                                    
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
                            nodosConEtiqueta,aristaConEtiquetas=actualizar(nodos,aristas)
                            if Diferencia< 20:
                                if nodo in aux:
                                    continue
                                else:
                                    aux.append(nodo)
                                if (len(aux)==2):
                                    pygame.draw.line(ventana,BLANCO,aux[0],aux[1])
                                    if digraph==True:
                                        if(aux[0][0]<aux[1][0]):
                                            ventana.blit(imagenflecha, [((aux[0][0]+aux[1][0])/2)+10,(aux[0][1]+aux[1][1])/2])
                                        else:
                                            imagenflechaRotada=pygame.transform.rotate(imagen4, 180)
                                            ventana.blit(imagenflechaRotada, [(aux[0][0]+aux[1][0])/2,(aux[0][1]+aux[1][1])/2])
                                    if aux in aristas:
                                        aux=[]
                                        break
                                    else:
                                        aristas.append(aux)
                                    if digraph==False:
                                        aristas.append([aux[1],aux[0]])
                                    aux=[]
                                break

                    elif(visitar==True):
                        nodosConEtiqueta,aristaConEtiquetas=actualizar(nodos,aristas)
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
                                if(len(NodosInicioFinal)==0):
                                    pygame.draw.circle(ventana,VERDE,nodo,20)
                                    NodosInicioFinal.append(nodo)
                                if(len(NodosInicioFinal)==1 and NodosInicioFinal[0] != nodo):
                                    pygame.draw.circle(ventana,VERDE,NodosInicioFinal[0],20)
                                    pygame.draw.circle(ventana,[0,0,255],nodo,20)
                                    NodosInicioFinal.append(nodo)
                                    nodosDelCamino=camino([nodosConEtiqueta,aristaConEtiquetas],nodosConEtiqueta[nodos.index(NodosInicioFinal[0])],
                                        nodosConEtiqueta[nodos.index(NodosInicioFinal[1])])
                                    
                                    if nodosDelCamino !=[]:
                                        rutas=obtenerRutas(nodosDelCamino)
                                        for ruta in rutas:
                                            arista=aristas[aristaConEtiquetas.index(ruta)]
                                            pygame.time.delay(500)
                                            pygame.draw.line(ventana,[250,0,0],arista[0],arista[1])
                                            pygame.display.flip()
                                            pygame.time.delay(500)
                                            pygame.draw.circle(ventana,ROJO,arista[1],20)
                                            pygame.display.flip()
                                        pygame.draw.circle(ventana,AZUL,NodosInicioFinal[1],20)
                                    else:
                                        mjs="Sin ruta"
                                        pygame.draw.rect(ventana, NEGRO, [400,8,500,25])
                                        fuente_texto=pygame.font.Font(None,25)
                                        info=fuente_texto.render(mjs,True,BLANCO)
                                        ventana.blit(info,[1000,15])
                                    NodosInicioFinal=[]
                                break
                    elif(conexo==True and event.pos[0] > 208 and event.pos[0] < 308 and event.pos[1] > 9 and event.pos[1] < 35):
                        nodosConEtiqueta,aristaConEtiquetas=actualizar(nodos,aristas)
                        #Para saber si es conexo
                        if(len(nodosConEtiqueta)==0):
                            mjs="El grafo no tiene nodos"
                            ubicacionTexto=[500,8]

                        elif (len(aristaConEtiquetas)<(len(nodosConEtiqueta)-1)):
                            mjs="No es conexo, numero de aristas menores a los nodos- 1"
                            ubicacionTexto=[400,8]

                        elif(isconexo(nodosConEtiqueta,aristaConEtiquetas)==True):
                            mjs="El grafo es conexo"
                            ubicacionTexto=[500,8]
                        else:
                            mjs="El grafo es no conexo"
                            ubicacionTexto=[500,8]
                        pygame.draw.rect(ventana, NEGRO, [400,8,500,25])
                        fuente_texto=pygame.font.Font(None,25)
                        info=fuente_texto.render(mjs,True,BLANCO)
                        ventana.blit(info,ubicacionTexto)
                        pygame.display.flip()
                    
                    elif(bipartito==True and event.pos[0] > 208 and event.pos[0] < 308 and event.pos[1] > 9 and event.pos[1] < 35):
                        nodosConEtiqueta,aristaConEtiquetas=actualizar(nodos,aristas)
                        if (len(nodosConEtiqueta)==0):
                            mjs="El Grafo no tiene nodos"
                        elif (isconexo(nodosConEtiqueta,aristaConEtiquetas)==True):
                            if(isBiopartido(nodosConEtiqueta,aristaConEtiquetas)==True):
                                mjs="El grafo es bipartito"
                            else:
                                mjs="El grafo no es bipartito"
                        else:
                            mjs="El grafo no es bipartito"
                        pygame.draw.rect(ventana, NEGRO, [400,8,500,25])
                        fuente_texto=pygame.font.Font(None,25)
                        info=fuente_texto.render(mjs,True,BLANCO)
                        ventana.blit(info,[500,8])
                        pygame.display.flip() 

                    elif(euleriano==True and event.pos[0] > 208 and event.pos[0] < 308 and event.pos[1] > 9 and event.pos[1] < 35):
                        nodosConEtiqueta,aristaConEtiquetas=actualizar(nodos,aristas)
                        if (len(nodosConEtiqueta)==0):
                            mjs="El Grafo no tiene nodos"
                            ubicacion=[500,8]
                        else:
                            isEulerian=esEuleriano(nodosConEtiqueta,aristaConEtiquetas)
                            if (type(isEulerian)==type(fin)):
                                caminoStr=""
                                circuit1=circuitoHamiltoniano(aristaConEtiquetas,nodosConEtiqueta)
                                circuit1.reverse()
                                mjs="El grafo es euleriano"
                                ubicacion=[500,8]
                            else:
                                mjs="El grafo no es euleriano incosistencia en el nodo " + isEulerian[1]
                                ubicacion=[400,8]
                        pygame.draw.rect(ventana, NEGRO, [400,8,450,25])
                        fuente_texto=pygame.font.Font(None,25)
                        info=fuente_texto.render(mjs,True,BLANCO)
                        ventana.blit(info,ubicacion)
                        pygame.display.flip()
                    #Hamiltoniano
                    elif(euleriano==True and event.pos[0] > 870 and event.pos[0] < 990 and event.pos[1] > 9 and event.pos[1] < 35):
                        nodosConEtiqueta,aristaConEtiquetas=actualizar(nodos,aristas)
                        if (len(nodosConEtiqueta)==0):
                            mjs="El Grafo no tiene nodos"
                            ubicacion=[500,8]
                        else:
                            isEulerian=esEuleriano(nodosConEtiqueta,aristaConEtiquetas)
                            if (type(isEulerian)==type(fin)):
                                caminoStr=""
                                circuit1=circuitoHamiltoniano(aristaConEtiquetas,nodosConEtiqueta)
                                circuit1.reverse()
                                destinos=obtenerRutas(circuit1)

                                repeticion=[]
                                for destino in destinos:
                                    arista=aristas[aristaConEtiquetas.index([destino[0],destino[1]])]
                                    if [destino[0],destino[1]] in repeticion or [destino[1],destino[0]] in repeticion :
                                        pygame.time.delay(500)
                                        pygame.draw.line(ventana,VERDE,arista[0],arista[1])
                                        pygame.display.flip()
                                        pygame.time.delay(500)
                                        pygame.draw.circle(ventana,VERDE,arista[1],20)
                                        pygame.display.flip()
                                        if ([destino[0],destino[1]] in repeticion):repeticion.remove([destino[0],destino[1]])
                                        else:repeticion.remove([destino[1],destino[0]])
                                    else:
                                        pygame.time.delay(500)
                                        pygame.draw.line(ventana,[250,0,0],arista[0],arista[1])
                                        pygame.display.flip()
                                        pygame.time.delay(500)
                                        pygame.draw.circle(ventana,ROJO,arista[1],20)
                                        pygame.display.flip()
                                    repeticion.append([destino[0],destino[1]])



                                mjs="El grafo es euleriano"
                                ubicacion=[500,8]
                            else:
                                mjs="El grafo no es euleriano incosistencia en el nodo " + isEulerian[1]
                                ubicacion=[400,8]
                        pygame.draw.rect(ventana, NEGRO, [400,8,450,25])
                        fuente_texto=pygame.font.Font(None,25)
                        info=fuente_texto.render(mjs,True,BLANCO)
                        ventana.blit(info,ubicacion)
                        pygame.display.flip()  


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
                        if Diferencia < 20 and agregarNodo==True:
                            pygame.draw.circle(ventana,NEGRO,nodo,20)
                            nodos.remove(nodo)
                            """for arista in aristas:
                                if arista[0] is nodo or arista[1] is nodo:
                                    print("Somos iguales")
                                if nodo in arista:

                                    aristas.remove(arista)
                                    pygame.draw.line(ventana,NEGRO,arista[0],arista[1])
                                    ventana.blit(imagenflechaBorrar, [((arista[0][0]+arista[1][0])/2)+10,(arista[0][1]+arista[1][1])/2])
                                    imagenflechaRotada=pygame.transform.rotate(imagen6, 180)
                                    ventana.blit(imagenflechaRotada, [(arista[0][0]+arista[1][0])/2,(arista[0][1]+arista[1][1])/2])
                        break"""
                    if(agregarArista==True):                          
                        for arista in aristas:
                            pendiente=(arista[0][0]-arista[1][0])/(arista[0][1]-arista[1][1])
                            limiteinferior=pendiente-0.2
                            limiteSuperior=pendiente+0.2
                            pendiente2=(arista[0][0]-event.pos[0]+0.1)/(arista[0][1]-event.pos[1]+0.1)

                            if pendiente2>limiteinferior and pendiente2<limiteSuperior and agregarArista==True:
                                pygame.draw.line(ventana,NEGRO,arista[0],arista[1])
                                aristas.remove(arista)
                                if([arista[1],arista[0]] in aristas):
                                    aristas.remove([arista[1],arista[0]])
                                ventana.blit(imagenflechaBorrar, [((arista[0][0]+arista[1][0])/2)+10,(arista[0][1]+arista[1][1])/2])
                                imagenflechaRotada=pygame.transform.rotate(imagen6, 180)
                                ventana.blit(imagenflechaRotada, [(arista[0][0]+arista[1][0])/2,(arista[0][1]+arista[1][1])/2])
                                #Si es dirigido
                                #aristas.remove([arista[1],arista[0]])
                                break
                                    
            if event.type == pygame.KEYDOWN:
                G=nx.Graph()
                if event.key == pygame.K_a:
                    letraInicial=65
                    nodosConEtiqueta=[]
                    aristaConEtiquetas=[]
                    for nodo in nodos:
                        nodosConEtiqueta.append(chr(letraInicial))
                        pygame.draw.circle(ventana,BLANCO,nodo,20)
                        fuente_J=pygame.font.Font(None,32)
                        mjs=chr(letraInicial)
                        info=fuente_J.render(mjs,True,NEGRO)
                        ventana.blit(info,nodo)
                        letraInicial+=1
                    G.add_nodes_from(nodosConEtiqueta)
                    for arista in aristas:
                        v1=nodosConEtiqueta[nodos.index(arista[0])] 
                        v2=nodosConEtiqueta[nodos.index(arista[1])]
                        aristaConEtiquetas.append([v1,v2])
                    G.add_edges_from(aristaConEtiquetas)
                    nodosColoreados=colorearMapa(nodosConEtiqueta,aristaConEtiquetas)
                    for indexNodo in range(len(nodos)):
                        pygame.draw.circle(ventana,
                            nodosColoreados[indexNodo],
                            nodos[indexNodo],
                            20)  
                    print(colorearMapa(nodosConEtiqueta,aristaConEtiquetas))
                    
                    
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


            if(agregarNodo==True):
                pygame.draw.rect(ventana, NEGRO, [1000,2,1200,40])
                pygame.draw.rect(ventana, NEGRO, [200,2,800,40])
                pygame.draw.rect(ventana, BLANCO, [200,2,800,40],5,10)
                ventana.blit(imgMouseDerecho, [750, 3])
                mjs="Eliminar nodo"
                fuente_tutorial=pygame.font.Font(None,18)
                info=fuente_tutorial.render(mjs,True,BLANCO)
                ventana.blit(info,[780,15])
                ventana.blit(imgMouseIzquierda, [400, 3])
                mjs="Agregar nodo"
                fuente_tutorial=pygame.font.Font(None,18)
                info=fuente_tutorial.render(mjs,True,BLANCO)
                ventana.blit(info,[320,15])

            if(agregarArista==True):
                pygame.draw.rect(ventana, NEGRO, [1000,2,1200,40])
                pygame.draw.rect(ventana, NEGRO, [200,2,800,40])
                pygame.draw.rect(ventana, BLANCO, [200,2,800,40],5,10)
                ventana.blit(imgMouseDerecho, [750, 3])
                mjs="Eliminar arista"
                fuente_tutorial=pygame.font.Font(None,18)
                info=fuente_tutorial.render(mjs,True,BLANCO)
                ventana.blit(info,[780,15])
                ventana.blit(imgMouseIzquierda, [400, 3])
                mjs="Agregar arista"
                fuente_tutorial=pygame.font.Font(None,18)
                info=fuente_tutorial.render(mjs,True,BLANCO)
                ventana.blit(info,[320,15])
                if(len(aux)==1):
                    mjs="Nodo origen --> "+nodosConEtiqueta[nodos.index(aux[0])]
                    fuente_texto=pygame.font.Font(None,25)
                    info=fuente_texto.render(mjs,True,BLANCO)
                    ventana.blit(info,[500,15])

            if(visitar==True):
                pygame.draw.rect(ventana, NEGRO, [200,2,800,40])
                pygame.draw.rect(ventana, BLANCO, [200,2,800,40],5,10)
                pygame.draw.circle(ventana,AZUL,[750, 22],14)
                mjs="Nodo Final"
                fuente_tutorial=pygame.font.Font(None,18)
                info=fuente_tutorial.render(mjs,True,BLANCO)
                ventana.blit(info,[780,15])
                pygame.draw.circle(ventana,VERDE,[420, 22],14)
                mjs="Nodo Inicial"
                fuente_tutorial=pygame.font.Font(None,18)
                info=fuente_tutorial.render(mjs,True,BLANCO)
                ventana.blit(info,[320,15])

                mjs="Seleccionar"
                fuente_J=pygame.font.Font(None,32)
                info=fuente_J.render(mjs,True,BLANCO)
                ventana.blit(info,[530,10])

            if(conexo==True or bipartito==True or euleriano==True):
                accion=pygame.mouse.get_pos()
                pygame.draw.rect(ventana, NEGRO, [1000,2,1200,40])
                if euleriano==True:
                    if (accion[0] > 208 and accion[0] < 308 and accion[1] > 9 and accion[1] < 35):
                        pygame.draw.rect(ventana,BLANCO,[208,9,100,26],2,50)
                        mjs="Verificar"
                        fuente_texto=pygame.font.Font(None,25)
                        info=fuente_texto.render(mjs,True,BLANCO)
                        ventana.blit(info,[223,13])
                    elif (accion[0] > 870 and accion[0] < 990 and accion[1] > 9 and accion[1] < 35):
                        pygame.draw.rect(ventana,BLANCO,[870,9,120,26],2,50)
                        mjs="Hamiltoniano"
                        fuente_texto=pygame.font.Font(None,25)
                        info=fuente_texto.render(mjs,True,BLANCO)
                        ventana.blit(info,[875,13])
                    else:
                        pygame.draw.rect(ventana, BLANCO, [200,2,800,40],5,10)
                        pygame.draw.rect(ventana, ROJO, [208,9,100,26])
                        pygame.draw.rect(ventana,NEGRO,[208,8,100,27],2,50)
                        pygame.draw.rect(ventana, ROJO, [870,9,120,26])
                        pygame.draw.rect(ventana, NEGRO, [870,8,120,27],2,50)

                        mjs="Verificar"
                        fuente_texto=pygame.font.Font(None,25)
                        info=fuente_texto.render(mjs,True,NEGRO)
                        ventana.blit(info,[223,13])
                        mjs="Hamiltoniano"
                        fuente_texto=pygame.font.Font(None,25)
                        info=fuente_texto.render(mjs,True,NEGRO)
                        ventana.blit(info,[875,13])
                else:
                    if (accion[0] > 208 and accion[0] < 308 and accion[1] > 9 and accion[1] < 35):
                        pygame.draw.rect(ventana,BLANCO,[208,9,100,26],2,50)
                        mjs="Verificar"
                        fuente_texto=pygame.font.Font(None,25)
                        info=fuente_texto.render(mjs,True,BLANCO)
                        ventana.blit(info,[223,13])
                    else:
                        pygame.draw.rect(ventana, BLANCO, [200,2,800,40],5,10)
                        pygame.draw.rect(ventana, ROJO, [208,9,100,26])
                        pygame.draw.rect(ventana,NEGRO,[208,8,100,27],2,50)
                        mjs="Verificar"
                        fuente_texto=pygame.font.Font(None,25)
                        info=fuente_texto.render(mjs,True,NEGRO)
                        ventana.blit(info,[223,13])

            pygame.display.flip()
