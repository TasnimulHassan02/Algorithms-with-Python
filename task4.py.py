input4 = open("C:\\Users\\jadid hossain\\Dropbox\\My PC (LAPTOP-Q2RHKRMQ)\\Desktop\\LAB3\\input4.txt", 'r')
output4 = open("C:\\Users\\jadid hossain\\Dropbox\\My PC (LAPTOP-Q2RHKRMQ)\\Desktop\\LAB3\\output4.txt", 'w')


def partition(arr, p, r):
    pivot = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def find_kth(arr, p, r, k):
    if p == r:
        return arr[p]
    pivot_index = partition(arr, p, r)
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return find_kth(arr, p, pivot_index - 1, k)
    else:
        return find_kth(arr, pivot_index + 1, r, k)

N = int(input4.readline())
arr = list(map(int, input4.readline().split()))
Q = int(input4.readline())
for _ in range(Q):
    K = int(input4.readline())
    kth_smallest = find_kth(arr, 0, N - 1, K - 1)
    output4.write(f"{kth_smallest}\n")

input4.close()
output4.close()



