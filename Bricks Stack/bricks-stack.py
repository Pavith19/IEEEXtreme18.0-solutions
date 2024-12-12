"""
Author: Pavith Bambaravanage
URL: https://github.com/Pavith19
"""
import sys
import heapq

def main():
    input = sys.stdin.read
    data = input().splitlines()

    brick_count, height_diff = map(int, data[0].split())
    brick_lengths = list(map(int, data[1].split()))

    brick_lengths.sort()
    stacks = []

    for length in brick_lengths:
        if stacks and stacks[0][0] + height_diff <= length:
            top_length, stack = heapq.heappop(stacks)
            stack.append(length)
            heapq.heappush(stacks, (length, stack))
        else:
            new_stack = [length]
            heapq.heappush(stacks, (length, new_stack))

    print(len(stacks))
    for _, stack in stacks:
        print(len(stack), *sorted(stack, reverse=True))

if __name__ == "__main__":
    main()
