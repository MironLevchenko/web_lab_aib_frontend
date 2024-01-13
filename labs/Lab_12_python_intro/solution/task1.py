def count_routes(N, M):
    arr = [[0] * (M+1) for _ in range(N+1)]
    arr[1][1] = 1
    for i in range(2, N + 1):
        for j in range(2, M + 1):
            arr[i][j] = arr[i - 1][j - 2] + arr[i - 2][j - 1]
    return arr[N][M]
if __name__ == '__main__':
    N = int(input("Enter number of lines N : "))
    M = int(input("Enter number of columns M : "))
    result = count_routes(N, M)
    print("Number of different routes: ", result)