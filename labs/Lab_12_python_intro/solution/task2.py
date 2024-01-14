<<<<<<< HEAD
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
=======
from heapq import heappop, heappush

def subarrays_medians_sum(numbers: list):
    medians_sum = 0
    smallerHalf, largerHalf = [], []
    for number in numbers:
        heappush(smallerHalf, -number)
        heappush(largerHalf, -heappop(smallerHalf))
        if len(smallerHalf) < len(largerHalf):
            heappush(smallerHalf, -heappop(largerHalf))
        medians_sum += -smallerHalf[0]
    return medians_sum

if __name__ == '__main__':
    numbers = [int(number) for number in input().split()][1:]
    print(subarrays_medians_sum(numbers))
>>>>>>> 8ca2eeef386c20360bbb5f6b8ed0abfe4c98dbf7
