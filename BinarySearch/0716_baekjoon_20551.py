import time


def overlap(arr, mid):
    while arr[mid] == arr[mid-1]:
        mid -= 1
    return mid


def binSearch(arr, t):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low+high) // 2
        if arr[mid] == t:
            return overlap(arr, mid)
        elif arr[mid] < t:
            low = mid+1
        else:
            high = mid-1
    return -1


N, M = map(int, input().split())

A = [int(input()) for _ in range(N)]
D = [int(input()) for _ in range(M)]

print('<<<result>>>')
start = time.time()

B = sorted(A)
for i in D:
    print(binSearch(B, i))

print("time :", time.time() - start)
