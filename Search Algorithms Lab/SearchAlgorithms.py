from matplotlib.artist import get
from matplotlib.pyplot import close
from numpy import VisibleDeprecationWarning
from Space import *
from Constants import *
import time

def drawLine(g:Graph,a,b,sc:pygame.Surface):
    if(a.value!=g.start.value and a.value!=g.goal.value):
        a.set_color(grey)
        a.draw(sc)
    if(b.value!=g.start.value and b.value!=g.goal.value):
        b.set_color(grey)
        b.draw(sc)
    pygame.draw.line(sc, green, (a.x,a.y), (b.x,b.y))
    pygame.display.flip()
def DFS(g:Graph, sc:pygame.Surface):
    print('Implement DFS algorithm')
    
    open_set = [g.start] #cac node mo rong den
    closed_set = [] #cac node di qua
    father = [-1]*g.get_len() #tu x mo rong dc y father[x]=y
  
    #TODO: Implement DFS algorithm using open_set, closed_set, and father
    while open_set:
        node=open_set.pop()
        node.set_color(yellow)
        node.draw(sc)
        time.sleep(0.05)
        pygame.display.flip()

        if node not in closed_set:
            node.set_color(blue)
            time.sleep(0.05)
            node.draw(sc)
            pygame.display.flip()
            closed_set.append(node)
            if g.is_goal(node):
                g.start.set_color(orange)
                g.start.draw(sc)
                g.goal.set_color(purple)
                g.goal.draw(sc)
                v=node.value
                while father[v]!=g.start.value:
                    drawLine(g,g.grid_cells[v],g.grid_cells[father[v]],sc)
                    v=father[v]
                drawLine(g,g.grid_cells[v],g.grid_cells[father[v]],sc)
                break
            for neigbor in g.get_neighbors(node):
                if neigbor not in closed_set:
                    father[neigbor.value]=node.value
                    neigbor.set_color(red)
                    neigbor.draw(sc)
                    time.sleep(0.05)
                    pygame.display.flip()
                    open_set.append(neigbor)
    


def BFS(g:Graph, sc:pygame.Surface):
    print('Implement BFS algorithm')

    open_set = [g.start]
    closed_set = []
    father = [-1]*g.get_len()

    #TODO: Implement BFS algorithm using open_set, closed_set, and father
    while open_set:
        node=open_set.pop(0)
        node.set_color(yellow)
        node.draw(sc)
        time.sleep(0.05)
        pygame.display.flip()

        node.set_color(blue)
        time.sleep(0.05)
        node.draw(sc)
        pygame.display.flip()
        if g.is_goal(node):
            g.start.set_color(orange)
            g.start.draw(sc)
            g.goal.set_color(purple)
            g.goal.draw(sc)
            v=node.value
            while father[v]!=g.start.value:
                drawLine(g,g.grid_cells[v],g.grid_cells[father[v]],sc)
                v=father[v]
            drawLine(g,g.grid_cells[v],g.grid_cells[father[v]],sc)  
            break
        for neighbor in g.get_neighbors(node):
            if neighbor not in closed_set:
                father[neighbor.value]=node.value
                neighbor.set_color(red)
                neighbor.draw(sc)
                time.sleep(0.05)
                pygame.display.flip()
                open_set.append(neighbor)
                closed_set.append(neighbor)


def get_weight(node):
    return 1
def UCS(g:Graph, sc:pygame.Surface):
    print('Implement UCS algorithm')

    # open_set = {} 
    # open_set[g.start.value] = 0
    # closed_set:list[int] = []
    closed_set=[] 
    open_set =[g.start]
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len() 
    cost[g.start.value] = 0
    #TODO: Implement UCS algorithm using open_set, closed_set, and father
    while open_set:
        curr=None
        for v in open_set:
            if curr is None or cost[curr.value]>cost[v.value]:
                curr=v
        curr.set_color(yellow)
        curr.draw(sc)
        time.sleep(0.05)
        pygame.display.flip()
        curr.set_color(blue)
        time.sleep(0.05)
        curr.draw(sc)
        pygame.display.flip()
        if g.is_goal(curr):
            g.start.set_color(orange)
            g.start.draw(sc)
            g.goal.set_color(purple)
            g.goal.draw(sc)
            v=curr.value
            while father[v]!=g.start.value:
                drawLine(g,g.grid_cells[v],g.grid_cells[father[v]],sc)
                v=father[v]
            drawLine(g,g.grid_cells[v],g.grid_cells[father[v]],sc)
            break
        open_set.remove(curr)
        closed_set.append(curr)
        for neighbor in g.get_neighbors(curr):
            if neighbor not in closed_set:
                neighbor.set_color(red)
                time.sleep(0.05)
                neighbor.draw(sc)
                pygame.display.flip()
                if neighbor not in open_set:
                    father[neighbor.value]=curr.value
                    open_set.append(neighbor)
                elif cost[curr.value]<cost[neighbor.value]:
                    cost[neighbor]=cost[curr]

def heuristic(a, b) -> float:
    (x1, y1) = (a.x,a.y)
    (x2, y2) = (b.x,b.y)
    return abs(x1 - x2) + abs(y1 - y2)
def AStar(g:Graph, sc:pygame.Surface):
    print('Implement A* algorithm')

    # open_set = {}
    # open_set[g.start.value] = 0
    # closed_set:list[int] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0
    open_set=[g.start]
    closed_set=[]
    #TODO: Implement A* algorithm using open_set, closed_set, and father

    while open_set:
        curr=None
        for v in open_set:
            if curr is None or cost[curr.value]+heuristic(curr,g.goal)>cost[v.value]+heuristic(v,g.goal):
                curr=v
        curr.set_color(yellow)
        curr.draw(sc)
        time.sleep(0.05)
        pygame.display.flip()
        curr.set_color(blue)
        time.sleep(0.05)
        curr.draw(sc)
        pygame.display.flip()
        if g.is_goal(curr):
            g.start.set_color(orange)
            g.start.draw(sc)
            g.goal.set_color(purple)
            g.goal.draw(sc)
            v=curr.value
            while father[v]!=g.start.value:
                drawLine(g,g.grid_cells[v],g.grid_cells[father[v]],sc)
                v=father[v]
            drawLine(g,g.grid_cells[v],g.grid_cells[father[v]],sc)
            break
        open_set.remove(curr)
        closed_set.append(curr)
        for neighbor in g.get_neighbors(curr):
            if neighbor not in closed_set:
                neighbor.set_color(red)
                time.sleep(0.05)
                neighbor.draw(sc)
                pygame.display.flip()
                if neighbor not in open_set:
                    father[neighbor.value]=curr.value
                    open_set.append(neighbor)
                elif cost[curr.value]<cost[neighbor.value]:
                    cost[neighbor]=cost[curr]

    # raise NotImplementedError('Not implemented')