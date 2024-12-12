def solve(N, Q, P, queries):
    # Initialize array A with zeros
    A = [0] * N
    
    # Process each query
    results = []
    for query in queries:
        query_type = query[0]
        
        if query_type == 0 or query_type == 1:  # Update operations
            l, r, c = query[1:]
            # Adjust indices for 0-based indexing
            l -= 1
            r -= 1
            
            if query_type == 0:  # Update consecutive elements
                for i in range(l, r + 1):
                    A[i] += c
            else:  # Update elements based on permutation
                for i in range(l, r + 1):
                    A[P[i] - 1] += c
                    
        else:  # Query operations (type 2 or 3)
            l, r = query[1:]
            # Adjust indices for 0-based indexing
            l -= 1
            r -= 1
            
            if query_type == 2:  # Sum of consecutive elements
                result = sum(A[l:r + 1])
            else:  # Sum of permuted elements
                result = sum(A[P[i] - 1] for i in range(l, r + 1))
            
            results.append(result)
    
    return results

# Process input
def main():
    # Read N and Q
    N, Q = map(int, input().split())
    
    # Read permutation P
    P = list(map(int, input().split()))
    
    # Read queries
    queries = []
    for _ in range(Q):
        query = list(map(int, input().split()))
        queries.append(query)
    
    # Solve and output results
    results = solve(N, Q, P, queries)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
