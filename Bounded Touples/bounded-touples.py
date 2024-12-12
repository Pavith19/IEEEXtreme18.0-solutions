"""
Author: Pavith Bambaravanage
URL: https://github.com/Pavith19
"""
from typing import List, Tuple
from dataclasses import dataclass

@dataclass
class Constraint:
    low: int
    high: int
    indices: List[int]

def solve_variable_constraints(N: int, M: int, constraints: List[Constraint]) -> str:
    MOD = 998244353
    MAX_SEARCH = 50  
    
    def check_infinite() -> bool:
        used_vars = set()
        for c in constraints:
            for idx in c.indices:
                used_vars.add(idx)
        return len(used_vars) < N
    
    def is_valid_assignment(values: List[int]) -> bool:
        for c in constraints:
            sum_vars = sum(values[idx-1] for idx in c.indices)
            if not (c.low <= sum_vars <= c.high):
                return False
        return True
    
    def count_valid_assignments(curr_values: List[int], pos: int) -> int:
        if pos == N:
            return 1 if is_valid_assignment(curr_values) else 0
            
        count = 0
        for val in range(MAX_SEARCH):
            curr_values[pos] = val
            can_continue = True
            for c in constraints:
                if all(idx-1 <= pos for idx in c.indices):
                    sum_vars = sum(curr_values[idx-1] for idx in c.indices)
                    if not (c.low <= sum_vars <= c.high):
                        can_continue = False
                        break
            
            if can_continue:
                count = (count + count_valid_assignments(curr_values, pos + 1)) % MOD
                
        return count
    
    if check_infinite():
        return "infinity"
    
    result = count_valid_assignments([0] * N, 0)
    return str(result)

def main():
    N, M = map(int, input().split())
    
    constraints = []
    for _ in range(M):
        line = list(map(int, input().split()))
        low, high, K = line[0], line[1], line[2]
        indices = line[3:3+K]
        constraints.append(Constraint(low, high, indices))
    
    result = solve_variable_constraints(N, M, constraints)
    print(result)

def run_test():
    test_input = """3 2
0 4 2 1 2
3 5 2 2 3"""
    

    lines = test_input.strip().split('\n')
    
    N, M = map(int, lines[0].split())
    
    constraints = []
    for i in range(M):
        line = list(map(int, lines[i + 1].split()))
        low, high, K = line[0], line[1], line[2]
        indices = line[3:3+K]
        constraints.append(Constraint(low, high, indices))
    
    result = solve_variable_constraints(N, M, constraints)
    print(f"Test case result: {result}")

if __name__ == "__main__":
    main()
    
