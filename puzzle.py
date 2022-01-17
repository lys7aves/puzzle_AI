from queue import PriorityQueue
import copy
import time

def init():
    curr = [[1,2,6], ['*',4,3], ['*',7,5]]
    goal = [[1,2,3], ['*','*',4], [7,6,5]]
    return [curr, goal]

def Where(puzzle):
    where = {}
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if(puzzle[i][j] == 0):
                continue
            where[puzzle[i][j]] = (i,j)
            
    return where

def switchPuzzle(puzzle, i, j, ii, jj):
    newPuzzle = copy.deepcopy(puzzle)
    tmp = newPuzzle[i][j]
    newPuzzle[i][j] = newPuzzle[ii][jj]
    newPuzzle[ii][jj] = tmp
    
    return newPuzzle

def Move(puzzle, i, j):
    moves = []
    if(i > 0):
        moves.append(switchPuzzle(puzzle, i, j, i-1, j))
    if(i < len(puzzle)-1):
        moves.append(switchPuzzle(puzzle, i, j, i+1, j))
    if(j > 0):
        moves.append(switchPuzzle(puzzle, i, j, i, j-1))
    if(j < len(puzzle[0])-1):
        moves.append(switchPuzzle(puzzle, i, j, i, j+1))
    
    return moves

def Distance(curr, goal):
    where = Where(goal)
    
    distance = 0
    for i in range(len(curr)):
        for j in range(len(curr[0])):
            if(curr[i][j] == 0):
                continue
            (ii, jj) = where[curr[i][j]]
            distance = distance + abs(i-ii) + abs(j-jj)
    
    return distance

def starToZero(puzzle):
    tmp = copy.deepcopy(puzzle)
    for i in range(len(tmp)):
        for j in range(len(tmp[0])):
            if(tmp[i][j] == '*'):
                tmp[i][j] = 0
    
    return tmp

def AStarAlgorithm(curr, goal):
    start_time = time.time()
    print('----- start to A* alogrithm -----')
    curr = starToZero(curr)
    goal = starToZero(goal)
    puzzle_size = len(curr) * len(curr[0])
    
    que = PriorityQueue()
    que.put([0, curr, []])
    
    Time = 0
    memory = puzzle_size
    
    while(not que.empty()):
        Time = Time + 1
        memory = max(memory, que.qsize()*puzzle_size)
        
        [curr, path] = que.get()[1:3]
        if(curr == goal):
            print('find!')
            for puzzle in path:
                print(puzzle)
            break
        
        flag = False
        for i in range(len(curr)):
            for j in range(len(curr[0])):
                if(curr[i][j] == 0):
                    moves = Move(curr, i, j)
                    for move in moves:
                        if(move == curr):
                            continue
                        
                        distance = Distance(curr, goal)
                        
                        path_ = copy.deepcopy(path)
                        path_.append(move)
                        
                        que.put([distance+len(path), move, path_])
                
    print('A* Algorithm')
    print('time : ', Time)
    print('memory : ', memory)
    print('real time : ', time.time() - start_time)
    print()
    
    return [Time, memory]

def IterativeDeepeningSearch(curr, goal):
    start_time = time.time()
    print('----- start to Iterative Deepening Search -----')
    Time = 0
    memory = 0
    
    limit = 0
    while(1):
        [Time_, memory_, flag] = DFS(curr, goal, 0, limit)
        
        Time = Time + Time_
        memory = max(memory, memory_)
        
        print(limit, Time, memory, flag)
        
        if(flag):
            break;
        
        limit = limit+1
        
    
                
    print('Iterative Deepening Search')
    print('time : ', Time)
    print('memory : ', memory)
    print('real time : ', time.time() - start_time)
    
    return [Time, memory]

def DFS(curr, goal, depth, limit):
    puzzle_size = len(curr) * len(curr[0])
    
    if(depth > limit):
        return [0, 0, False]
    if(curr == goal):
        return [1, puzzle_size, True]
    
    Time = 1
    memory = 0
    for i in range(len(curr)):
        for j in range(len(curr[0])):
            if(curr[i][j] == '*'):
                moves = Move(curr, i, j)
                for move in moves:
                    if(move == curr):
                        continue
                    [Time_, memory_, flag] = DFS(move, goal, depth+1, limit)
                    
                    Time = Time + Time_
                    memory = max(memory, memory_)
                    if(flag):
                        return [Time, memory+puzzle_size, True]
                    
    return [Time, memory+puzzle_size, False]

def main():
    [curr, goal] = init()
    AStarAlgorithm(curr, goal)
    IterativeDeepeningSearch(curr, goal)

main()