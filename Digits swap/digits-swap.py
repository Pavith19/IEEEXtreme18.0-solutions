"""
Author: Pavith Bambaravanage
URL: https://github.com/Pavith19
"""
import heapq

def maximize_number(N, K):
    digits = list(str(N))
    length = len(digits)
    
    max_heap = []
    heapq.heappush(max_heap, (-N, digits, 0))
    
    max_number = N
    max_possible_number = int(''.join(sorted(digits, reverse=True)))
    
    best_seen = {}
    
    while max_heap:
        current_neg_number, current_digits, swaps = heapq.heappop(max_heap)
        current_number = -current_neg_number

        max_number = max(max_number, current_number)

        if current_number == max_possible_number:
            break

        if swaps >= K:
            continue

        for i in range(length):
            for j in range(i + 1, length):
                current_digits[i], current_digits[j] = current_digits[j], current_digits[i]

                if current_digits[0] != '0':
                    new_number = int(''.join(current_digits))
                    
                    if new_number > max_number:
                        new_state = ''.join(current_digits)
                        if new_state not in best_seen or new_number > best_seen[new_state]:
                            best_seen[new_state] = new_number
                            heapq.heappush(max_heap, (-new_number, current_digits[:], swaps + 1))

                current_digits[i], current_digits[j] = current_digits[j], current_digits[i]

    return max_number

N, K = map(int, input().split())
print(maximize_number(N, K))
