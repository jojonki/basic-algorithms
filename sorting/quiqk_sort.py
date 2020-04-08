"""quick sort
"""

import random


# def quick_sort(arr, ascending=True):
#     if len(arr) <= 1: return arr
#     pid = random.randint(0, len(arr)-1)
#     pv = arr[pid]
#     left, right = [], []
#     for i in range(len(arr)):
#         if i == pid: continue
#         if arr[i] < pv:
#             if ascending:
#                 left.append(arr[i])
#             else:
#                 right.append(arr[i])
#         else:
#             if ascending:
#                 right.append(arr[i])
#             else:
#                 left.append(arr[i])
#
#     return quick_sort(left, ascending=ascending) + [pv] + quick_sort(right, ascending=ascending)

def quick_sort(arr, left=None, right=None, ascending=True):
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1
    if right <= left: return

    l, r = left, right

    pivot_id = l + (r - l) // 2
    pivot_v = arr[pivot_id]
    while True:
        if ascending:
            while arr[l] < pivot_v:
                l += 1
            while pivot_v < arr[r]:
                r -= 1
        else:
            while arr[l] > pivot_v:
                l += 1
            while pivot_v > arr[r]:
                r -= 1
        if l >= r: break
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

    quick_sort(arr, left, l-1, ascending=ascending)
    quick_sort(arr, r+1, right, ascending=ascending)


def main():
    test_data = [
        [3,4,7,3,76,9,3],
        [1,6,0,3,5,4,2,1,45,6,8,9],
        [1],
        [1,2,3,4],
        [4,3,2,1],
    ]

    print('ASCENDING')
    for t in test_data:
        print('----------')
        print('In :', t)
        quick_sort(t)
        print('Out:',t)

    print('DESCENDING')
    for t in test_data:
        print('----------')
        print('In :', t)
        quick_sort(t, ascending=False)
        print('Out:', t)


if __name__ == '__main__':
    main()

