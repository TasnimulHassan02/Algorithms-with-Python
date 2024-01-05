input2 = open("C:\\Users\\jadid hossain\\Dropbox\\My PC (LAPTOP-Q2RHKRMQ)\\Desktop\\LAB3\\input2.txt", 'r')
output2 = open("C:\\Users\\jadid hossain\\Dropbox\\My PC (LAPTOP-Q2RHKRMQ)\\Desktop\\LAB3\\output2.txt", 'w')

def max_value(arr, N):    
    i, i_item = 0, arr[0]
    j, j_item = 0, arr[1]    
    for x in range(1, N):
        if arr[x] >= 0 and arr[x] >= j_item:
            j = x
            j_item = arr[x]
        elif arr[x] < 0 and (arr[x] * -1) >= j_item:
            j = x
            j_item = (arr[x] * -1)    
    for x in range(j):
        if arr[x] >= i_item:
            i_item = arr[x]
            
    return i_item + j_item**2

N = int(input2.readline())
arr = list(map(int, input2.readline().split()))
output2.write(f"{max_value(arr, N)}")
input2.close()
output2.close()



