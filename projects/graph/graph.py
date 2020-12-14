"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v_from, v_to):
        if v_from in self.vertices and v_to in self.vertices:
            self.vertices[v_from].add(v_to)
            
    def is_connected(self, v_from, v_to):
        if v_from in self.vertices and v_to in self.vertices:
            return v_to in self.vertices[v_from]
        else:
            raise IndexError('nonexistant vertex')

    def get_neighbors(self, vertex_id):
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise IndexError('nonexistant vertext')

    def bft(self, starting_vertex):
        queue = []
        visited = set()
        queue.append(starting_vertex)
        
        while len(queue) != 0:
            vert = queue.pop(0)
            if vert not in visited:
                print(vert, self.get_neighbors(vert))
                visited.add(vert)
                for n in self.get_neighbors(vert):
                    queue.append(n)

    def dft(self, starting_vertex):
        stack = []
        visited = set()
        stack.append(starting_vertex)
        
        while len(stack) != 0:
            vert = stack.pop()
            if vert not in visited:
                print(vert, self.get_neighbors(vert))
                visited.add(vert)
                for n in self.get_neighbors(vert):
                    stack.append(n)

    def dft_recursive(self, starting_vertex, visited = set()):
        visited.add(starting_vertex)
        print(starting_vertex)
        for next_vert in self.get_neighbors(starting_vertex):
            if next_vert not in visited:     
                self.dft_recursive(next_vert, visited)
        

    def bfs(self, starting_vertex, destination_vertex):
        queue = []
        visited = set()
        queue.append([starting_vertex])
        
        while len(queue) != 0:
            path = queue.pop(0)
            if path[-1] not in visited:
                if path[-1] == destination_vertex:
                    return path
                visited.add(path[-1])
                for n in self.get_neighbors(path[-1]):
                    queue.append(path + [n])
        return None
        
    def dfs(self, starting_vertex, destination_vertex):
        stack = []
        visited = set()
        stack.append([starting_vertex])
        
        while len(stack) != 0:
            path = stack.pop()
            if path[-1] not in visited:
                if path[-1] == destination_vertex:
                    return path
                visited.add(path[-1])
                for n in self.get_neighbors(path[-1]):
                    stack.append(path + [n])
        return None

    def dfs_recursive(self, starting_vertex, target, visited = set(), path=None):
        
        if path is None:
            path = [starting_vertex]
            
        visited.add(starting_vertex)
        
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                new_path = path + [neighbor]
                if neighbor == target:
                    return new_path   
                dfs_path = self.dfs_recursive(neighbor, target, visited, new_path)
                if dfs_path is not None:
                    return dfs_path
        return None
            
            
if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)
    # graph.dft_recursive(1)
    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # print(graph.dfs_recursive(1, 5))

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
