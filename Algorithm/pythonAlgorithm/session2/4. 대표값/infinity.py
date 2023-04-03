arr = [5,3,7,9,2,5,2,6]
arrMin = float('inf') # 무한수 infinity
for i in range(len(arr)):
    if arr[i] < arrMin:
        arrMin = arr[i]
        print(arrMin)
        
arrmin = arr[0]
for i in range(1,len(arr)):
    if arr[i] < arrmin:
        arrmin = arr[i]
        print(arrmin)