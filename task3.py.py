input3 = open("C:\\Users\\jadid hossain\\Dropbox\\My PC (LAPTOP-Q2RHKRMQ)\\Desktop\\LAB3\\input3.txt", 'r')
output3 = open("C:\\Users\\jadid hossain\\Dropbox\\My PC (LAPTOP-Q2RHKRMQ)\\Desktop\\LAB3\\output3.txt", 'w')

def partition(arr, p, r):
	pivot = arr[r]
	i = p - 1
	for j in range(p, r):
		if arr[j] <= pivot:
			i = i + 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i + 1], arr[r] = arr[r], arr[i + 1]
	
	return i + 1

def quick_sort(arr, p, r):	
	if p < r:
		q = partition(arr, p, r)
		quick_sort(arr, p, q - 1)
		quick_sort(arr, q + 1, r)
		
	return arr

N = int(input3.readline())
arr = list(map(int, input3.readline().split()))
output3.write(' '.join(list(map(str, quick_sort(arr, 0, N-1)))))
input3.close()
output3.close()