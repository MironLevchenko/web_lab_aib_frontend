import heapq
def find(n, arr):
    max = []
    min = []
    result = 0
    for i in range(n):
        heapq.heappush(max, -arr[i])
        heapq.heappush(min, -heapq.heappop(max))
        if len(min) > len(max):
            heapq.heappush(max, -heapq.heappop(min))
        result -= max[0]
    return result
n, arr = int(input()), list(map(int, input().split()))
print(find(n, arr))