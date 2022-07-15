import time


def lowerbound(arr, t):
    low, high = 0, len(arr)

    while low < high:
        mid = (low+high) // 2
        if arr[mid] >= t:
            high = mid
        else:
            low = mid + 1
    return low


N, M = map(int, input().split())

A = [int(input()) for _ in range(N)]
D = [int(input()) for _ in range(M)]

print('<<<result>>>')
start = time.time()

B = sorted(A)
for i in D:
    index = lowerbound(B, i)
    if index < N and B[index] == i:
        print(index)
    else:
        print(-1)


print("time :", time.time() - start)
