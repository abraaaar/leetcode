"""
Insertion Sort Time Complexity: Worst: O(n^2) Best: O(n)
                                Space Complexity: O(1)

"""

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > key:
#             arr[j+1] = arr[j]
#             j -= 1
#             arr[j+1] = key





def insertion_sort(arr):
    for i in range(1, len(arr)):
        cur = arr[i]
        j=i-1
        while j>=0 and arr[j] > cur:
            arr[j+1] = arr[j]
            arr[j] = cur
            j -= 1


arr = [12, 11, 13, 5, 6, 19, 4, 0, 1, 7, 8, 1000]
print("Original array is:", arr)
insertion_sort(arr)
print("Sorted array is:", arr)
