# Իրականացնել բինար որոնման ալգորիթմը զանգվածի համար իտերատիվ տարբերակով։

def bs(arr, target):
    left = 0 
    right = len(arr) - 1 
    
    while left <= right:
        mid = (left + right) // 2 
        
        if arr[mid] == target: 
            return mid
        elif arr[mid] < target: 
            left = mid + 1
        else:
            right = mid - 1
    return -1  

arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
result = bs(arr, target)

if result != -1:
    print(result)
else:
    print("None found")
