def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * (y // gcd(x, y))

def count_hit_tiles(N, elasticities):
    from itertools import combinations

    K = len(elasticities)
    total_tiles_hit = 0

    for i in range(1, 1 << K):  
        subset_lcm = 1
        bits_count = 0

        for j in range(K):
            if i & (1 << j):  
                bits_count += 1
                subset_lcm = lcm(subset_lcm, elasticities[j])
                if subset_lcm > N:  
                    break

        if subset_lcm <= N:
            count = N // subset_lcm
            if bits_count % 2 == 1: 
                total_tiles_hit += count
            else:  
                total_tiles_hit -= count

    return total_tiles_hit

N, K = map(int, input().split())
elasticities = list(map(int, input().split()))

result = count_hit_tiles(N, elasticities)

print(result)
