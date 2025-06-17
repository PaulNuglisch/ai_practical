from myqueue import Queue
from graph import Node, Edge, Graph

def cool():
    print("cool")

# def bfs(graph, start, goal):
#     if start == goal or not graph.contains(start) or not graph.contains(goal):
#         return "INVALID INPUT"
    
#     startNode = graph.get(start)
#     goalNode = graph.get(goal)
        
#     frontier = Queue('FIFO')
#     frontier.push(startNode)
#     explored = Queue()
#     path = Queue()
    
#     while not frontier.is_empty():
#         node = frontier.pop()
#         explored.push(node)
        
#         parent = node
        
#         for edge in node.edges:
  
#             child = edge[1]
#             if not explored.contains(child) and not frontier.contains(child):
#                 if child == goalNode:
#                     child.parent = parent
#                     graph.print_path(child)
#                     return graph
                
#                 child.parent = parent
#                 frontier.push(child)
    
    
#     print("NODE NOT FOUND")            
#     return -1