def b_search(arr, x):
	low = 0
	high = len(arr) - 1
	mid = 0
	while low <= high:
		mid = (high + low) // 2
		if arr[mid] < x:
			low = mid + 1
		elif arr[mid] > x:
			high = mid - 1
		elif arr[mid] == x:
			return mid
	return -1

arr = [ 7, 9, 10, 13, 19, 30]
x = 10
result = b_search(arr, x)
if result != -1:
	print("Element index = ", str(result))
else:
	print("Element not in array")
