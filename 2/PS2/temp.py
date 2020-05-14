class Node(object):
    """Represents a node in the graph"""
    def __init__(self, name):
        self.name = str(name)

    def get_name(self):
        return self.name

class WeightedEdge(object):
    def __init__(self, src, dest, total_distance, outdoor_distance):
        self.src=src
        self.dest=dest
        self.total_distance = total_distance
        self.outdoor_distance = outdoor_distance

    def get_total_distance(self):
        return self.total_distance

    def get_outdoor_distance(self):
        return self.outdoor_distance
    
    def get_source(self):
        return self.src

    def get_destination(self):
        return self.dest

    def __str__(self):
        return '{}->{} ({}, {})'.format(self.get_source().get_name(), \
         self.get_destination().get_name(), str(self.total_distance), \
          str(self.outdoor_distance))  

class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        for key,value in self.__graph_dict.items():
            return str(key) +'-->'+str(value[0])+' Time='+str(value[1])+' Time outside='+str(value[2])
    # def get_start(self):
    # def get_end(self):
    #     return 
    # def get_time(self):
    # def get_outtime(self):

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res
    def find_path(self, start_vertex, end_vertex, path=None):
        """ find a path from start_vertex to end_vertex 
            in graph """
        if path == None:
            path = []
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex,end_vertex,path)
                if extended_path: 
                    return extended_path
        return None
    
    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        """ find all paths from start_vertex to 
            end_vertex in graph """
        graph = self.__graph_dict 
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex,end_vertex,path)                                   
                for p in extended_paths: 
                    
                    paths.append(p)
        return paths
    
    def find_best_path(self, start_vertex, end_vertex, path=[]):
        """ find all paths from start_vertex to 
            end_vertex in graph """
        shortest=None
        graph = self.__graph_dict 
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
       
        for vertex in graph[start_vertex]:
            if vertex not in path:
                if shortest == None or len(path) < len(shortest):
                    extended_paths = self.find_best_path(vertex,end_vertex,path)                                   
                    if extended_paths!=None:
                        shortest=extended_paths
        return shortest
    
   
    
    def printPath(path):
        """Assumes path is a list of nodes"""
        result = ''
        path=path[0]
        for i in range(len(path)):
            result = result + str(path[i])
            if i != len(path) - 1:
                result = result + '->'
        return result 
    
    




maps={}
with open('mit_map.txt','r') as file:
    for line in file:
        x=line.split(' ')
        
        if int(x[0]) not in maps:
            maps[int(x[0])]=[]
        maps[int(x[0])].append(int(x[1]))
        
print(maps)

# graph = Graph(maps)

# # print("Vertices of graph:")
# # print(graph.vertices())

# path=graph.find_best_path(32, 35)
# print('Shortest Path from 32 to 35')
# # print(path)

# print(Graph.printPath(path))
# # print(Graph.printPath(path))



















