def linear_search(arr, number_to_find):
    for index, element in enumerate(arr):
        if element == number_to_find:
            return index
    return -1


def binary_search(arr, number_to_find):
    left_index = 0
    right_index = len(arr) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = arr[mid_index]

        if mid_number == number_to_find:
            return mid_index
        
        if mid_number < number_to_find:
            left_index = mid_index + 1
        
        else:
            right_index = mid_index - 1


if __name__ == '__main__':
    arr = [1, 4, 5, 6, 7, 10, 15]
    print(binary_search(arr, 1))
