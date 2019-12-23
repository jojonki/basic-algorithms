"""Bubble sort
"""

def bubble_sort(arr, left_pt=0, ascending=True):
    for i in range(len(arr)-1, left_pt, -1):
        compare = None
        if ascending:
            compare = arr[i-1] < arr[i]
        else:
            compare = arr[i-1] > arr[i]
        if not compare:
            tmp = arr[i]
            arr[i] = arr[i-1]
            arr[i-1] = tmp

    left_pt += 1
    if left_pt == len(arr):
        return
    else:
        bubble_sort(arr, left_pt, ascending=ascending)


def main():
    test_data = [
        [3,4,7,3,76,9,3],
        [1],
        [1,2,3,4],
        [4,3,2,1],
    ]

    print('ASCENDING')
    for t in test_data:
        print('----------')
        print('In :', t)
        bubble_sort(t)
        print('Out:',t)

    print('DESCENDING')
    for t in test_data:
        print('----------')
        print('In :', t)
        bubble_sort(t, ascending=False)
        print('Out:', t)


if __name__ == '__main__':
    main()