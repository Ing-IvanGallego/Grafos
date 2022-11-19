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

def esEuleriano(nodos, edges):
    euleriana=True
    vecinos=[0]*len(nodos)
    for (nodoinicio,nodoFinal) in edges:
        vecinos[nodos.index(nodoinicio)]+=1
        vecinos[nodos.index(nodoFinal)]+=1
    for vecinoNodo in vecinos:
        print(vecinos)
        if (vecinoNodo%2==1):
            euleriana=False
            return euleriana,nodos[vecinos.index(vecinoNodo)]
            break
    return euleriana
def printCircuito(edges,nodos):
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
                         print(grupos)
                         grupos[grupo].append(nodo)
                     else: continue
             else:
                 continue
         cualGrupo=grupo
         asignacionGrupo(nodos,vecinos,visitados,cualGrupo,grupos)

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

     return grupos

     return asignacionGrupo(nodos,vecinos,visitados,1,grupos)



alto,ancho=1000,700
fin=False
BLANCO = 255,255,255
NEGRO=0,0,0
ROJO=[255,0,0]
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


if __name__ == '__main__':
    pygame.init()
    reloj=pygame.time.Clock()
    ventana=pygame.display.set_mode([alto,ancho])
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

    
    iconoConexo="C"
    fuente_J=pygame.font.Font(None,32)
    pygame.draw.circle(ventana,ROJO,(20,140),20)
    info=fuente_J.render(iconoConexo,True,NEGRO)
    ventana.blit(info,[15,135])




    while(fin==False):
    	for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

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
                        pygame.draw.circle(ventana,[0,255,0],(20,20),20)
                        ventana.blit(imagenNodo, [10, 10])
                        pygame.draw.circle(ventana,ROJO,(20,60),20)
                        ventana.blit(imagenArista, [5, 58])
                        pygame.draw.circle(ventana,ROJO,(20,100),20)
                        ventana.blit(imagenvisitar, [5, 80])
                        pygame.draw.circle(ventana,ROJO,(20,140),20)
                        info=fuente_J.render(iconoConexo,True,NEGRO)
                        ventana.blit(info,[15,135])

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
                        pygame.draw.circle(ventana,[0,255,0],(20,60),20)
                        ventana.blit(imagenArista, [5, 58])
                        pygame.draw.circle(ventana,ROJO,(20,20),20)
                        ventana.blit(imagenNodo, [10, 10])
                        pygame.draw.circle(ventana,ROJO,(20,100),20)
                        ventana.blit(imagenvisitar, [5, 80])
                        pygame.draw.circle(ventana,ROJO,(20,140),20)
                        info=fuente_J.render(iconoConexo,True,NEGRO)
                        ventana.blit(info,[15,135])

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
                        pygame.draw.circle(ventana,ROJO,(20,60),20)
                        ventana.blit(imagenArista, [5, 58])
                        pygame.draw.circle(ventana,ROJO,(20,20),20)
                        ventana.blit(imagenNodo, [10, 10])
                        pygame.draw.circle(ventana,[0,255,0],(20,100),20)
                        ventana.blit(imagenvisitar, [5, 80])
                        pygame.draw.circle(ventana,ROJO,(20,140),20)
                        info=fuente_J.render(iconoConexo,True,NEGRO)
                        ventana.blit(info,[15,135])
                    elif event.pos[0]<40 and event.pos[1]>80 and event.pos[1]<120 and visitar==True:
                         visitar=False
                         pygame.draw.circle(ventana,ROJO,(20,100),20)
                         ventana.blit(imagenvisitar, [5, 80])

                    elif event.pos[0]<40 and event.pos[1]>120 and event.pos[1]<160 and conexo==False:
                        agregarArista=False
                        agregarNodo=False
                        visitar=False
                        conexo=True
                        euleriano=False
                        pygame.draw.circle(ventana,ROJO,(20,60),20)
                        ventana.blit(imagenArista, [5, 58])
                        pygame.draw.circle(ventana,ROJO,(20,20),20)
                        ventana.blit(imagenNodo, [10, 10])
                        pygame.draw.circle(ventana,ROJO,(20,100),20)
                        ventana.blit(imagenvisitar, [5, 80])
                        pygame.draw.circle(ventana,[0,255,0],(20,140),20)
                        info=fuente_J.render(iconoConexo,True,NEGRO)
                        ventana.blit(info,[15,135])

                    elif event.pos[0]<40 and event.pos[1]>120 and event.pos[1]<160 and conexo==True:
                         conexo=False
                         pygame.draw.circle(ventana,ROJO,(20,140),20)
                         info=fuente_J.render(iconoConexo,True,NEGRO)
                         ventana.blit(info,[15,135])
                    
                         
                    elif (agregarNodo==True):
                        if len(nodos)==0:
                            nodos.append(event.pos)
                            pygame.draw.circle(ventana,BLANCO,event.pos,20)
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
                            if Diferencia< 20:
                                if nodo in aux:
                                    break
                                else:
                                    aux.append(nodo)

                                if (len(aux)==2):
                                    pygame.draw.line(ventana,BLANCO,aux[0],aux[1])
                                    if(aux[0][0]<aux[1][0]):
                                        ventana.blit(imagenflecha, [((aux[0][0]+aux[1][0])/2)+10,(aux[0][1]+aux[1][1])/2])
                                    else:
                                        imagenflechaRotada=pygame.transform.rotate(imagen4, 180)
                                        ventana.blit(imagenflechaRotada, [(aux[0][0]+aux[1][0])/2,(aux[0][1]+aux[1][1])/2])
                                    if aux in aristas or [aux[1],aux[0]] in aristas:
                                        aristas.append(aux)
                                        #continue
                                    else:
                                        aristas.append(aux)
                                        #aristas.append([aux[1],aux[0]])
                                    aux=[]
                                break
                    elif(visitar==True):
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
                                    pygame.draw.circle(ventana,[0,255,0],nodo,20)
                                    NodosInicioFinal.append(nodo)

                                if(len(NodosInicioFinal)==1 and NodosInicioFinal[0] != nodo):
                                    
                                    pygame.draw.circle(ventana,[0,0,255],nodo,20)
                                    NodosInicioFinal.append(nodo)
                                    nodosDelCamino=camino([nodosConEtiqueta,aristaConEtiquetas],nodosConEtiqueta[nodos.index(NodosInicioFinal[0])],
                                        nodosConEtiqueta[nodos.index(NodosInicioFinal[1])])
                                    NodosInicioFinal=[]
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
                                break
                    elif(conexo==True):
                        G=nx.Graph()
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

                        print("Estos son los nodos ", G.nodes)
                        print("Estos son las aristas", G.edges)
                        #Para saber si es conexo
                        if (len(G.edges)<(len(G.nodes(G))-1)):
                            print("No es conexo debido a que el minimo de aristas deben ser  de n-1")
                        elif(isconexo(nodosConEtiqueta,aristaConEtiquetas)==False):
                            print("no conexo")
                        else:
                            print("Es conexo")
                        


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
                            for arista in aristas:
                                print(arista,"nodo--->",nodo)
                                if arista[0]==nodo or arista[1]==nodo:
                                    aristas.remove(arista)
                                    pygame.draw.line(ventana,NEGRO,arista[0],arista[1])




                            
                    for arista in aristas:
                        pendiente=(arista[0][0]-arista[1][0])/(arista[0][1]-arista[1][1])
                        limiteinferior=pendiente-0.2
                        limiteSuperior=pendiente+0.2
                        pendiente2=(arista[0][0]-event.pos[0]+0.1)/(arista[0][1]-event.pos[1]+0.1)
                        if pendiente2>limiteinferior and pendiente2<limiteSuperior and agregarArista==True:
                            pygame.draw.line(ventana,NEGRO,arista[0],arista[1])
                            aristas.remove(arista)
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

                    print("Estos son los nodos ", G.nodes)
                    print("Estos son las aristas", G.edges)
                    
                    if (isconexo(nodosConEtiqueta,aristaConEtiquetas)==True):
                        print( "Es bipartido ",isBiopartido(nodosConEtiqueta,aristaConEtiquetas))
                    else:
                        print("No es bipartido")
   
                    """
                    isEulerian=esEuleriano(nodosConEtiqueta,aristaConEtiquetas)
                    print("Funcion euleriana ",isEulerian)
                    if isEulerian==True:
                        destinos=printCircuito(aristaConEtiquetas,nodosConEtiqueta)
                    #print(esEuleriano(Gmatrix.todense()))
                    if (isEulerian==True):
                        #source=="A" para empezar en el nodo que decee
                        destinos=list(nx.eulerian_circuit(G))
                        print(destinos)
                        repeticion=[]
                        for destino in destinos:
                            arista=aristas[aristaConEtiquetas.index([destino[0],destino[1]])]
                            if [destino[0],destino[1]] in repeticion or [destino[1],destino[0]] in repeticion :
                                pygame.time.delay(500)
                                pygame.draw.line(ventana,[0,255,0],arista[0],arista[1])
                                pygame.display.flip()
                                pygame.time.delay(500)
                                pygame.draw.circle(ventana,[0,255,0],arista[1],20)
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
                    else:
                        print("No es eulerian_circuit")"""
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
