import sys
import heapq
from collections import defaultdict, deque

def project_order():
    n, m = map(int, sys.stdin.readline().strip().split())
    group_ids = list(map(int, sys.stdin.readline().strip().split()))
    
    adj = defaultdict(list)
    in_degree = [0] * n
    
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().strip().split())
        adj[a - 1].append(b - 1)
        in_degree[b - 1] += 1
    
    min_heap = []
    for i in range(n):
        if in_degree[i] == 0:
            heapq.heappush(min_heap, (group_ids[i], i))
    
    result = []
    while min_heap:
        _, project = heapq.heappop(min_heap)
        result.append(project + 1)
        
        for neighbor in adj[project]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                heapq.heappush(min_heap, (group_ids[neighbor], neighbor))
    
    if len(result) != n:
        print(-1)
    else:
        print(" ".join(map(str, result)))

project_order()
