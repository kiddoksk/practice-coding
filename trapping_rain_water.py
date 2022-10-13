def find_water(arr, n):
    # left has heighest of tallest bar to the left
    left = [0]*n

    # right has heighest of tallest bar to the right
    right = [0]*n

    water = 0

    # fill left array
    left[0] = arr[0]
    for i in range(1, n):
        left[i] = max(left[i-1], arr[i])
    
    # fill right array
    right[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        right[i] = max(right[i+1], arr[i])
    
    for i in range(0, n):
        water += min(left[i], right[i]) - arr[i]
    
    return water


if __name__ == '__main__':
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    n = len(arr)
    print(find_water(arr, n))