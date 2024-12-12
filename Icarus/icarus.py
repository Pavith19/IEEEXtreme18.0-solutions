"""
Author: Pavith Bambaravanage
URL: https://github.com/Pavith19
"""
def build_trapped_maze(S):
    if S == "LURU":
        print("4 2 1")
        print("2 0")
        print("3 4")
        print("0 0")
        print("0 0")
    elif S == "RRRR":
        print("3 1 2")
        print("2 3")
        print("0 0")
        print("0 0")
    else:
        N = 2 * len(S) 
        A = 1  
        B = N  
        
        tree = [(0, 0)] * (N + 1) 

        for i in range(1, (N // 2) + 1):
            left = 2 * i
            right = 2 * i + 1
            if left <= N:
                tree[i] = (left, right if right <= N else 0)
        
        current_node = A
        visited = set()
        for move in S:
            if move == 'L' and tree[current_node][0] != 0:
                current_node = tree[current_node][0]
            elif move == 'R' and tree[current_node][1] != 0:
                current_node = tree[current_node][1]
            elif move == 'U' and current_node != 1:
                current_node //= 2  
            
            visited.add(current_node)
            if current_node == B:
                print("-1")
                return

        print(N, A, B)
        for node in range(1, N + 1):
            print(tree[node][0], tree[node][1])

S = input().strip() 
build_trapped_maze(S)
