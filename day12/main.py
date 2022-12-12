from __future__ import annotations
from typing import Dict, List, Tuple
from heapq import heappop, heappush


class Node():

    def __init__(self, coordinates: Tuple[int, int]) -> None:
        self.coordinates: Tuple[int, int] = coordinates
        self.connections: List[self] = []

    def add_connection(self, node):
        self.connections.append(node)

    def __repr__(self) -> str:
        return f'<Node:{self.coordinates}>'

    def __str__(self) -> str:
        return str(self.coordinates)


class Graph():

    def __init__(self) -> None:
        self.nodes: Dict[Tuple[int, int], Node] = {}

    def get_or_create_node(self, coordinates: Tuple[int, int]) -> Node:
        if coordinates in self.nodes:
            return self.nodes[coordinates]
        else:
            self.nodes[coordinates] = Node(coordinates)
            return self.nodes[coordinates]

    def add_connection(self, a: Tuple[int, int], b: Tuple[int, int]):
        a: Node = self.get_or_create_node(a)
        b: Node = self.get_or_create_node(b)
        a.add_connection(b)

    def create_graph_from_matrix(self, matrix, rule):
        for x in range(len(matrix)-1):
            for y in range(len(matrix[0])-1):
                if(rule(matrix[x][y], matrix[x][y+1])):
                    self.add_connection((x, y), (x, y+1))
                if(rule(matrix[x][y+1],matrix[x][y])):
                    self.add_connection((x, y+1), (x, y))
                if(rule(matrix[x][y], matrix[x+1][y])):
                    self.add_connection((x, y), (x+1, y))
                if(rule(matrix[x+1][y], matrix[x][y])):
                    self.add_connection((x+1, y), (x, y))
        for i in range(len(matrix[0])-1):
            if rule(matrix[len(matrix)-1][i], matrix[len(matrix)-1][ i+1]):
                self.add_connection((len(matrix)-1, i), (len(matrix)-1, i+1))
            if rule(matrix[len(matrix)-1][i+1], matrix[len(matrix)-1][ i]):
                self.add_connection((len(matrix)-1, i+1), (len(matrix)-1, i))
        for i in range(len(matrix)-1):
            if(rule(matrix[i][len(matrix[0])-1],matrix[i+1][len(matrix[0])-1])):
                self.add_connection((i,len(matrix[0])-1), (i+1, len(matrix[0])-1))
            if(rule(matrix[i+1][len(matrix[0])-1],matrix[i][len(matrix[0])-1])):
                self.add_connection((i+1,len(matrix[0])-1), (i, len(matrix[0])-1))

    def find_shortest_path(self, start: Tuple[int, int], end: Tuple[int, int]):
        heap = []
        prev = {start: None}
        dist = {start: 0 }
        heappush(heap, (0, start))
        for distance, coordinates in heap:
            node:Node = self.get_or_create_node(coordinates)
            for neighbor in node.connections:
                if  dist.get(neighbor.coordinates,distance+2) > distance+1:
                    prev[neighbor.coordinates]= coordinates
                    dist[neighbor.coordinates]= distance+1
                    heappush(heap,(distance+1, neighbor.coordinates))
        return prev,dist 
       
def char_matrix_to_int_matrix(f):
    rows = []
    for row, line in enumerate(f.readlines()):
        line = line.strip()
        columns = []
        for col, char in enumerate(line):
            match char:
                case 'S':
                    columns.append(0)
                    start = (row, col)
                case 'E':
                    columns.append(26)
                    end = (row, col)
                case x:
                    columns.append(ord(x)-ord('a'))
        rows.append(columns)
    return start, end, rows


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        start, end, matrix = char_matrix_to_int_matrix(f)
        graph = Graph()
        graph.create_graph_from_matrix(matrix, lambda x, y: x >= y-1)
        prev, dist= graph.find_shortest_path(start,end)
        print(dist[end])
        starts=[]
        for x,v in enumerate(matrix):
            for y,h in enumerate(v):
                if h==0:
                    starts.append((x,y))
        print(len(starts))
        print(min(graph.find_shortest_path(s, end)[1].get(end,float('inf')) for s in starts))
            