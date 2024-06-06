import networkx as nx

from database.DAO import DAO
class Model:
    def __init__(self):
        self._grafo=nx.Graph()
        self._dizionario_opere={}
        pass

    def creaGrafo(self):
        self._grafo.clear()
        self._dizionario_opere = {}
        lista=DAO.getAllObject()
        for element in lista:
            self._grafo.add_node(element)
            self._dizionario_opere[element.object_id]=element
        listaedge=DAO.getConnessioni()
        for element in listaedge:
            if self._grafo.has_edge(self._dizionario_opere[element.object_id1],self._dizionario_opere[element.object_id2]):
                self._grafo[self._dizionario_opere[element.object_id1]][self._dizionario_opere[element.object_id2]]['weight']+=1
            else:
                self._grafo.add_edge(self._dizionario_opere[element.object_id1],self._dizionario_opere[element.object_id2],weight=1)
    def numNodi(self):
        return len(self._grafo.nodes())

    def numEdges(self):
        return len(self._grafo.edges())
    def controllo(self,id):
        if id in self._dizionario_opere.keys():
            return True
        else:
            return False

    def componente_connessa(self, id_oggetto):
        id=self._dizionario_opere[id_oggetto]
        edges = nx.bfs_edges(self._grafo, id)
        visited = []
        for u, v in edges:
            visited.append(v)
        return visited





