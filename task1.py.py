input1 = open("C:\\Users\\jadid hossain\\Dropbox\\My PC (LAPTOP-Q2RHKRMQ)\\Desktop\\LAB3\\input1.txt", 'r')
output1 = open("C:\\Users\\jadid hossain\\Dropbox\\My PC (LAPTOP-Q2RHKRMQ)\\Desktop\\LAB3\\output1.txt", 'w')




def counter(arr):
    if len(arr) == 1:
        return (arr, 0)
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    sorted_left, inversions_left = counter(left)
    sorted_right, inversions_right = counter(right)
    sorted_arr, inversions_merge = count_aliens(sorted_left, sorted_right)
    total_inversions = inversions_left + inversions_right + inversions_merge
    return (sorted_arr, total_inversions)

def count_aliens(left, right):
    sorted_arr = []
    inversions = 0
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            inversions += len(left) - i
            sorted_arr.append(right[j])
            j += 1
        else:
            sorted_arr.append(left[i])
            i += 1
    sorted_arr += left[i:]
    sorted_arr += right[j:]   
    return (sorted_arr, inversions)

N = int(input1.readline())
arr = list(map(int, input1.readline().split()))
sorted_heights, inversions = counter(arr)
output1.write(f"{inversions}")

input1.close()
output1.close()




