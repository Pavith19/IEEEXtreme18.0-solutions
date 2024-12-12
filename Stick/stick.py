
def calculate_union_area(N, K, L):
    single_square_area = (2 * L) ** 2
    
    if K > 2 * L:
        return N * single_square_area
    else:
        total_area = N * single_square_area - (N - 1) * (2 * L - K) ** 2
        return total_area

N, K, L = map(int, input().split())
print(calculate_union_area(N, K, L))

